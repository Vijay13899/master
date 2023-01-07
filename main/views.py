from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from  .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from .models import Calculation
# Create your views here.
def home(request):
    return render(request, 'home.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            username = form.cleaned_data.get("username")
            messages.success(request, "Account has been registered for "+username)
            return redirect('login')
    context = {'form': form, }
    return render(request,'register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password incorrect!')
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['master'])
def activityPage(request):
    if request.method == 'POST':
        calculation = request.POST.get('calculation')
        result = eval(calculation)  # evaluate the calculation and get the result
        Calculation.objects.create(calculation=calculation, result=result)  # save the calculation to the database
        context = {'result': result}
        return render(request, 'activity.html',context)
    return render(request,'activity.html')

@login_required(login_url='login')
def activitylog(request):
    calculations = Calculation.objects.all().order_by('-created_at')
    context = {'calculations':calculations}
    return render(request,'activitylog.html',context)


def zero(func=None):
    if func is None:
        return 0
    return func(0)

def one(func=None):
    if func is None:
        return 1
    return func(1)

def two(func=None):
    if func is None:
        return 2
    return func(2)

def three(func=None):
    if func is None:
        return 3
    return func(3)

def four(func=None):
    if func is None:
        return 4
    return func(4)

def five(func=None):
    if func is None:
        return 5
    return func(5)

def six(func=None):
    if func is None:
        return 6
    return func(6)

def seven(func=None):
    if func is None:
        return 7
    return func(7)

def eight(func=None):
    if func is None:
        return 8
    return func(8)

def nine(func=None):
    if func is None:
        return 9
    return func(9)

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x // y

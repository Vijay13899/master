from django.db import models
# Create your models here.


class Calculation(models.Model):
    calculation = models.CharField(max_length=255)
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

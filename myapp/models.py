from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    address = models.CharField(max_length = 100, null = True)
    phone = models.CharField(max_length = 30, null = True)
    gender = models.CharField(max_length = 10, null = True)
    birth = models.DateField(null = True)
    age = models.IntegerField(default = 0, blank = True, null = True)
    

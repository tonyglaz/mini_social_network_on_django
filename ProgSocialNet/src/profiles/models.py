from django.db import models
from django.contrib.auth.models import AbstractUser



class UserNet(AbstractUser):
    """custom user model"""
    middle_name=models.CharField(max_lenght=50)
    first_login=models.DateTimeField(null=True)
    phone = models.CharField(max_lenght=14)
    avatar=models.ImageField(uplooad_to='user/avatar.',blank=True,null=True)

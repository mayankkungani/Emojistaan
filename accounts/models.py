from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import User
#from django.contrib.auth import User
# Create your models here.


class UserProfiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    deaf=models.BooleanField(default=False)

    
    
   
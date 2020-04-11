from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfiles
#from .models import Profile



class Registerform(UserCreationForm):
    email=forms.EmailField()
    special=forms.BooleanField(required=False)

    class Meta:
        model=User
        fields=[
            'username','email','password','password2'
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfiles
        fields=['deaf']


"""
class UserUpdateform(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=[
            'username','email'
        ]

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']



"""        
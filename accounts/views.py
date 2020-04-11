from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
# Create your views here.

from django import forms
from .forms import Registerform,UserProfileForm
#from django.contrib import messages
'''
def login_page(request):

    form=Loginform(request.POST or None)
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"login.html",{})
'''
def register_page(request):
    if request.method=='POST':

        profile_form=UserProfileForm(request.POST or None)
        form=Registerform(request.POST or None)
        if form.is_valid() and profile_form.is_valid():
            #form.save()
            #form.save()
            user=form.save()
            print(user)
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            username=form.cleaned_data.get('username')
            #messages.success(request,f'account created for {username}!')
            return redirect('login')
    else:
        form=Registerform()
        profile_form=UserProfileForm()
    return render(request,'register.html',{'form':form,'profile_form':profile_form})
'''

def login(request):
    username ='username' in request.POST and request.POST['username']
    password ='password' in request.POST and request.POST['password']
    print(username,password)
    user = authenticate(username=username, password=password)
    return render(request,'login.html')
'''

def profile(request):
    return render(request,'profile.html')
#accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def loginPage(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # authenticated (SUCCESS)
            login(request,user)
            # return login(request,user)
            # redirect('viewer_homepage')
        else:
            messages.success(request, ("Error in logging in..."))
            # redirect to registration (AUTH FAILED)
            return redirect('register')

def registrationPage(request):
    if request.method=="GET":
        return render(request,'register.html')
    elif request.method=="POST":
        # create user and redirect to homepage
        pass
    
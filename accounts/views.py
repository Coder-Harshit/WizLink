#accounts/views.py
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def loginPage(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # authenticated (SUCCESS)
            login(request,user)
            return redirect('viewer_homepage')
        else:
            messages.success(request, ("Error in logging in..."))
            # redirect to registration (AUTH FAILED)
            return redirect('register')
    else:
        return render(request,'login.html')
    
def registrationPage(request):
    context = {}
    context['today'] = date.today()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('viewer_homepage')
    else:
        form = RegistrationForm()
    context['form'] = form        
    return render(request, 'register.html', context=context)

def logoutPage(request):
    logout(request)
    return redirect('login')
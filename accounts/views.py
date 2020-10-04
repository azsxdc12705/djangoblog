from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    # if request.method == "POST":
    # else:
        return render(request, 'accounts/signup.html')

def signin(request):
    # if request.method == "POST":  
    # else:
        return render(request, 'accounts/signin.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import UserProfile
from .forms import LoginForm, UserForm


# Create your views here.


def user_login(request):
    if request.method != "POST":
        return render(request, 'user/login.html')
        
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username = username).exists():
        messages.error(request, "Invalid username")
        return render(request, 'user/login.html')

    auth_value = authenticate(
        username = username,
        password = password
    )

    if auth_value is None:
        messages.error(request, "Invalid password")
        return render(request, 'user/login.html')
        
    return redirect('food:show')




def register(request):
    if request.method != "POST":
        return render(request, 'user/register.html')
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    conf_password = request.POST.get('c_password')

    if password != conf_password:
        messages.error(request, "password and confirm password are not matching")
        # return redirect('/register/') By using URL
        return redirect('register')

    user_data = User.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        email = email
        )
    user_data.set_password(password)
    user_data.save()
    
    messages.success(request, "User created successfully")
    return redirect('food:show')

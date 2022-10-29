import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# Isi Views

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("example_app:index"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Your Username or Password is Wrong!")
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "login.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Has Been Successfully Created!")
            return redirect("authenticate:login")
    
    context = { 
        "form": form,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("example_app:index"))
    response.delete_cookie("last_login")
    return response
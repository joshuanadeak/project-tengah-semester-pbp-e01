import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Isi Views
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("example_app:index"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return JsonResponse({
               "status": True,
               "message": "Successfully Logged In!"
               # Insert any extra data if you want to pass data to Flutter
             }, status=200)
        else:
            return JsonResponse({
               "status": False,
               "message": "Failed to Login, Account Disabled."
            }, status=401)
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "login.html", context)

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                'message': 'User successfully registered',
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            'message': 'Something went wrong',
            }, status=400)
    
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
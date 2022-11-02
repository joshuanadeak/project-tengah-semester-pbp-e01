from django.shortcuts import render
from .models import Quiz
from quiz.forms import QuizForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from crypto.forms import CryptoForm, NotesForm
from crypto.models import Crypto, Notes, Market
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def home(request):
    quiz = Quiz.objects.filter(user=request.user)
    context = {'quiz' : quiz}
    return render(request, 'home.html', context)

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def show_quiz(request):
    form = QuizForm()

    if request.method == "POST":
        form = QuizForm(request.POST)

    context = {'form':form}       
    return render(request, 'quiz.html', context)
    
@login_required(login_url='/authenticate/login/')
@csrf_exempt
def add_answer(request):
    skor = 0
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if (form.is_valid()):
            data_input = form.cleaned_data

            for i in data_input:
                if (data_input[i] == "True"):
                    skor=skor+10

    quiz = Quiz.objects.create(user=request.user, score=skor)
    return JsonResponse({'id': quiz.pk})

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def show_result(request, id):   
    return render(request, 'result.html')

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def result_json(request,id):
    if request.method == 'GET':
        data_quiz = Quiz.objects.get(pk = id)
    
    dict_data = {
        "user": data_quiz.user.username,
        "date": data_quiz.date,
        "score": data_quiz.score,
    }
    return JsonResponse(dict_data)


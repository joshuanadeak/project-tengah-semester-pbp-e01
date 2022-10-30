from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from stock.models import Saham

# Create your views here.
def show_stock(request):
    daftar_saham = Saham.objects.all()
    context = {
        'daftar_saham': daftar_saham
    }
    return render(request, "stock.html", context)



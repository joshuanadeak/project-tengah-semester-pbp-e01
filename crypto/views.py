from django.shortcuts import get_object_or_404, render
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
from crypto.forms import CryptoForm, NotesForm
from crypto.models import Crypto, Notes, Market
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @login_required(login_url='/authenticate/login/')
def show_crypto(request):
    daftar_crypto = Crypto.objects.all()
    context = {
        'nama': request.user.username,
        'daftar_crypto': daftar_crypto,
        'form': NotesForm
    }
    return render(request, "crypto.html", context)

# @login_required(login_url='/authenticate/login/')
def show_market(request):
    crypto_market = Market.objects.all()
    context = {
        'crypto_market': crypto_market,
        'form': CryptoForm
    }
    return render(request, "markets.html", context)

# @login_required(login_url='/authenticate/login/')
def show_crypto_json(request):
    crypto = Crypto.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", crypto), content_type="application/json")

# @login_required(login_url='/authenticate/login/')
def show_market_json(request):
    market = Market.objects.order_by('id')
    return HttpResponse(serializers.serialize("json", market), content_type="application/json")

# @login_required(login_url='/authenticate/login/')
@csrf_exempt
def add_crypto(request):
    form = CryptoForm(request.POST)
    if form.is_valid():
        kode_crypto = form.cleaned_data["kode_crypto"]
        nama_crypto = form.cleaned_data["nama_crypto"]
        harga_crypto = form.cleaned_data["harga_crypto"]
        risk = form.cleaned_data["risk"]
        new_crypto = Market.objects.create(kode_crypto = kode_crypto, nama_crypto = nama_crypto, harga_crypto = harga_crypto, risk = risk)
        return JsonResponse({'error': False, 'msg':'Successful'})

# @login_required(login_url='/authenticate/login/')
@csrf_exempt
def delete_crypto(request, stock_id):
    if request.method =="POST":
        delete_crypto = get_object_or_404(Crypto, pk=stock_id, user=request.user)
        new_market = Market.objects.create(kode_crypto = delete_crypto.kode_crypto, nama_crypto = delete_crypto.nama_crypto, harga_crypto = delete_crypto.harga_crypto, risk = delete_crypto.risk)
        delete_crypto.delete()
        return JsonResponse({'error':False})

# @login_required(login_url='/authenticate/login/')
@csrf_exempt
def delete_market(request, market_id):
    if request.method =="POST":
        delete_from_market = get_object_or_404(Market, pk=market_id)
        new_crypto = Crypto.objects.create(kode_crypto = delete_from_market.kode_crypto, nama_crypto = delete_from_market.nama_crypto, harga_crypto = delete_from_market.harga_crypto, risk = delete_from_market.risk, user = request.user)
        delete_from_market.delete()
        return JsonResponse({'error':False})

# @login_required(login_url='/authenticate/login/')
def show_notes_json(request):
    note = Notes.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", note), content_type="application/json")

# @login_required(login_url='/authenticate/login/')
def add_note(request):
    form = NotesForm(request.POST)
    if form.is_valid():
        note = form.cleaned_data["note"]
        delete_note = Notes.objects.filter(user=request.user)
        delete_note.delete()
        new_note = Notes.objects.create(note = note, user=request.user)
        return JsonResponse({'error': False, 'msg':'Successful'})
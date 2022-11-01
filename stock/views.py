from re import A
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
from stock.forms import StockForm, NoteForm
from stock.models import Saham, Pasar, Note
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/authenticate/login/')
def show_stock(request):
    daftar_saham = Saham.objects.filter(user=request.user)
    context = {
        'nama': request.user.username,
        'daftar_saham': daftar_saham,
        'form': NoteForm
    }
    return render(request, "stock.html", context)

@login_required(login_url='/authenticate/login/')
def show_market(request):
    pasar_saham = Pasar.objects.all()
    context = {
        'pasar_saham': pasar_saham,
        'form': StockForm
    }
    return render(request, "market.html", context)

@login_required(login_url='/authenticate/login/')
def show_stock_json(request):
    data_saham = Saham.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data_saham), content_type="application/json")

@login_required(login_url='/authenticate/login/')
def show_market_json(request):
    pasar_saham = Pasar.objects.order_by('id')
    return HttpResponse(serializers.serialize("json", pasar_saham), content_type="application/json")

@login_required(login_url='/authenticate/login/')
def show_note_json(request):
    note = Note.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", note), content_type="application/json")

@login_required(login_url='/authenticate/login/')
def add_stock(request):
    form = StockForm(request.POST)
    if form.is_valid():
        kode_saham = form.cleaned_data["kode_saham"]
        nama_perusahaan = form.cleaned_data["nama_perusahaan"]
        harga_saham = form.cleaned_data["harga_saham"]
        risk = form.cleaned_data["risk"]
        saham_baru = Pasar.objects.create(kode_saham = kode_saham, nama_perusahaan = nama_perusahaan, harga_saham = harga_saham, risk = risk)
        return JsonResponse({'error': False, 'msg':'Successful'})

@login_required(login_url='/authenticate/login/')
def add_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        catatan = form.cleaned_data["catatan"]
        note_del = Note.objects.filter(user=request.user)
        note_del.delete()
        note_baru = Note.objects.create(catatan = catatan, user=request.user)
        return JsonResponse({'error': False, 'msg':'Successful'})

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def delete_stock(request, stock_id):
    if request.method =="POST":
        stock_del = get_object_or_404(Saham, pk=stock_id, user=request.user)
        market_baru = Pasar.objects.create(kode_saham = stock_del.kode_saham, nama_perusahaan = stock_del.nama_perusahaan, harga_saham = stock_del.harga_saham, risk = stock_del.risk)
        stock_del.delete()
        return JsonResponse({'error':False})

@login_required(login_url='/authenticate/login/')
@csrf_exempt
def delete_market(request, market_id):
    if request.method =="POST":
        market_del = get_object_or_404(Pasar, pk=market_id)
        saham_baru = Saham.objects.create(kode_saham = market_del.kode_saham, nama_perusahaan = market_del.nama_perusahaan, harga_saham = market_del.harga_saham, risk = market_del.risk, user = request.user)
        market_del.delete()
        return JsonResponse({'error':False})

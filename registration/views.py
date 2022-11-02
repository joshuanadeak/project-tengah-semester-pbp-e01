from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from registration.forms import CompanyRegistrationForm

# Create your views here.
@login_required(login_url='/authenticate/login/')
def register_company(request):
    form = CompanyRegistrationForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registercompany.html', context)
    return render(request, 'registercompany.html', context)
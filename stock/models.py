from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Saham(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kode_saham = models.CharField(max_length=10, default="ABCD")
    nama_perusahaan = models.TextField(default="PT ABCD Tbk.")
    harga_saham = models.IntegerField()
    risk = models.CharField(max_length=10)

class Pasar(models.Model):
    kode_saham = models.CharField(max_length=10, default="ABCD")
    nama_perusahaan = models.TextField(default="PT ABCD Tbk.")
    harga_saham = models.IntegerField()
    risk = models.CharField(max_length=10)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catatan = models.TextField(default="jangan monopoli saham yaa")

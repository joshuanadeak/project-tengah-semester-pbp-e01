from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crypto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    kode_crypto = models.CharField(max_length=4, default="ETHS")
    nama_crypto = models.TextField(default="Ethnorium")
    harga_crypto = models.IntegerField()
    risk = models.TextField(max_length=10)

class Market(models.Model):
    kode_crypto = models.TextField(max_length=4, default="ETHS")
    nama_crypto = models.TextField(default="Ethnorium")
    harga_crypto = models.IntegerField()
    risk = models.TextField(max_length=10)

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(default="These are the notes for your crypto")
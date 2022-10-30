from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crypto(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    kode_crypto = models.TextField()
    harga_crypto = models.IntegerField()
    risk = models.TextField()

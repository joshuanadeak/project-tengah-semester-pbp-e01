from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Saham(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    kode_saham = models.TextField()
    harga_saham = models.IntegerField()
    risk = models.TextField()

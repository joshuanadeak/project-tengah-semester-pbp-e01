from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Company(models.Model):
    name = models.CharField(max_length = 255)
    price_of_stock = models.IntegerField(validators = [MinValueValidator(0)])
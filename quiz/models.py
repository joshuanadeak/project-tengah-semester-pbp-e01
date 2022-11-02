from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )
    date = models.DateTimeField(auto_now=True)
    score = models.FloatField(blank=True, null=True)

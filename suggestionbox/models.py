from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserFeedback(models.Model):
    feedback = models.TextField()
    reply = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
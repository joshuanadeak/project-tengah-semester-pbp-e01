from django.db import models

# Create your models here.
class UserFeedback(models.Model):
    feedback = models.TextField()
    reply = models.TextField()
    user = models.TextField(default="Anonymous")
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class DiscussionTitle(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def get_created_at(self):
        return self.created_at.strftime('%A, %d %b %Y')

class DiscussionReply(models.Model):
    reply = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion_title = models.ForeignKey(DiscussionTitle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def get_created_at(self):
        return self.created_at.strftime('%A, %d %b %Y')
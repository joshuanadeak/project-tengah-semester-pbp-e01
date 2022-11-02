from django.contrib import admin

# Register your models here.
from .models import DiscussionTitle, DiscussionReply

admin.site.register(DiscussionTitle)
admin.site.register(DiscussionReply)
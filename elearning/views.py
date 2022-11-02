import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from elearning.models import DiscussionTitle, DiscussionReply
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('elearning:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('elearning:discussions')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def show_discussions(request):
    discussions = DiscussionTitle.objects.all()
    logged_in = False
    is_empty = len(discussions) == 0
    if request.user.is_authenticated:
        logged_in = True
    context = {'logged_in':logged_in, 'is_empty':is_empty}
    return render(request, 'elearning.html', context)

@csrf_exempt
def add_discussion(request):
    title = request.POST.get('title')
    user = request.user
    DiscussionTitle.objects.create(title=title, user=user)
    return redirect('elearning:discussions')

@csrf_exempt
def add_reply(request, id):
    reply = request.POST.get('reply')
    discussion_title = DiscussionTitle.objects.get(id=id)
    user = request.user
    DiscussionReply.objects.create(reply=reply, user=user, discussion_title=discussion_title)
    return redirect('elearning:discussions')

def show_json(request):
    discussions = DiscussionTitle.objects.all()
    response = []
    for discussion in discussions:
        response.append({
            'id':discussion.id,
            'title':discussion.title,
            'user':discussion.user.username,
            'created_at':discussion.get_created_at()
        })
    return HttpResponse(json.dumps(response), content_type='application/json')

def show_reply_json(request, id):
    discussion = DiscussionTitle.objects.get(id=id)
    discussion_replies = DiscussionReply.objects.filter(discussion_title=id)
    replies = []
    for discussion_reply in discussion_replies:
        replies.append({
            'id':discussion_reply.id,
            'reply':discussion_reply.reply,
            'user':discussion_reply.user.username,
            'created_at':discussion_reply.get_created_at()
        })
    response = {
        "title" : discussion.title,
        "replies" : replies
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

def show_replies(request, id):
    discussion = DiscussionTitle.objects.get(id=id)
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    context = {'discussion':discussion,'logged_in':logged_in}
    return render(request, 'discussion_reply.html', context)

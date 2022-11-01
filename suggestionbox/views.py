from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from suggestionbox.models import UserFeedback
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def checkAdmin(user):
    return user.is_superuser

@login_required(login_url='/authenticate/login/')
def showFeedback(request):
    data  = UserFeedback.objects.all()
    return render(request, 'main_page.html', {'data': data})

def showJson(request):
    if request.method == 'GET':
        data = UserFeedback.objects.all()
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@user_passes_test(checkAdmin)
def replyFeedback(request, id):
    if request.method == 'POST':
        feedback = UserFeedback.objects.get(id=id)
        feedback.reply = request.POST['reply']
        if feedback.reply != '':
            feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")

@login_required(login_url='/authenticate/login/')
def giveFeedback(request):
    if request.method == 'POST':   
        feedback = UserFeedback(
            user = request.user,
            username=request.user.username,
            feedback = request.POST['feedback'],
            reply = 'Belum dibalas',
        )
        if feedback.feedback != '':
            feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")
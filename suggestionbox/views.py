from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from suggestionbox.models import UserFeedback
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def checkAdmin(user):
    return user.is_superuser

def showFeedback(request):
    data  = UserFeedback.objects.all()
    return render(request, 'main_page.html', {'data': data})

def showJson(request):
    data = UserFeedback.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@user_passes_test(checkAdmin)
def replyFeedback(request, id):
    if request.method == 'POST':
        feedback = UserFeedback.objects.get(id=id)
        feedback.reply = request.POST['reply']
        feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")

def giveFeedback(request):
    if request.method == 'POST':
        flag = False
        user = "Anonymous"
        if request.user.is_authenticated:
            flag = True
        if flag:
            user = request.user.username
        feedback = UserFeedback(
            user = user,
            feedback = request.POST['feedback'],
            reply = 'Belum dibalas',
        )
        feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")
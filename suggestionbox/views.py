from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from suggestionbox.models import UserFeedback
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
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
@csrf_exempt
def replyFeedback(request, id):
    if request.method == 'POST':
        feedback = UserFeedback.objects.get(id=id)
        feedback.reply = request.POST['reply']
        if feedback.reply != '':
            feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")

@csrf_exempt
def giveFeedback(request):
    if request.method == 'POST':
        username = ""
        try:
            username = request.POST['username']
        except:
            username = "Anonymous"
        feedback = UserFeedback(
            username=username,
            feedback = request.POST['feedback'],
            reply = 'Belum dibalas',
        )
        if feedback.feedback != '':
            feedback.save()
        return HttpResponse(serializers.serialize('json', [feedback]), content_type='application/json')
    return HttpResponse("")

@user_passes_test(checkAdmin)
@csrf_exempt
def deleteFeedback(request, id):
    if request.method == 'POST':
        data = get_object_or_404(UserFeedback, id=id)
        data.delete()
    return HttpResponse()

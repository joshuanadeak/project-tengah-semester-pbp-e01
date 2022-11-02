from django.urls import path
from quiz.views import show_quiz, home, show_result, add_answer, result_json
app_name = 'trivia'

urlpatterns = [
    path('', home, name='home'),
    path('start/', show_quiz, name='show_quiz'),
    path('result/<int:id>/', show_result, name='show_result'),
    path('add/', add_answer, name='add_answer'),
    path('json/<int:id>/', result_json, name='result_json'),
]

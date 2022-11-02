from django.urls import path
from elearning.views import register, add_reply, login_view, show_discussions, show_replies, add_discussion, show_json, show_reply_json

app_name = 'elearning'

urlpatterns = [
    path('', show_discussions, name='discussions'),
    path('register/', register, name='register'),
    path('add/', add_discussion, name='add_discussion'),
    path('login/', login_view, name='login'),
    path('discussions/', show_json, name='discussion_list'),
    path('discussion/<int:id>/', show_replies, name='discussion_reply'),
    path('discussion/<int:id>/json', show_reply_json, name='discussion_reply_json'),
    path('add_reply/<int:id>', add_reply, name='add_reply'),
]
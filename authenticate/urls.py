from django.urls import path
from authenticate.views import *

app_name = 'authenticate'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]
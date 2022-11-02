from django.urls import path
from registration.views import register_company

app_name = 'registration'

urlpatterns = [
    path('', register_company , name='registration'),
]
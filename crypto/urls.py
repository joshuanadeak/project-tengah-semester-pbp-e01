from django.urls import path
from crypto.views import show_crypto
app_name = 'crypto'

urlpatterns = [
    path('', show_crypto, name='show_crypto'),
]
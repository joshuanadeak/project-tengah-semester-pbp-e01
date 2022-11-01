from django.urls import path
from temp.views import register_company

app_name = 'stock'

urlpatterns = [
    path('', register_company , name='registration'),
]
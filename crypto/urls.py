from django.urls import path
from crypto.views import *
app_name = 'crypto'

urlpatterns = [
    path('', show_market, name='show_market'),
    path('porto', show_crypto, name='show_crypto'),
    path('mjson/', show_market_json, name='show_market_json'),
    path('delete_market/<int:market_id>', delete_market, name='delete_market'),
    path('add/', add_crypto, name='add_crypto'),
    path('delete_crypto/<int:stock_id>', delete_crypto, name='delete_crypto'),
    path('json/', show_crypto_json, name='show_crypto_json'),
    path('porto/add_note/', add_note, name='add_note'),
    path('porto/njson/', show_notes_json, name='show_notes_json'),
]
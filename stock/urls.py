from django.urls import path
from stock.views import show_stock,show_market, show_market_json, delete_market 
from stock.views import add_stock, delete_stock, show_stock_json
from stock.views import show_note_json, add_note

app_name = 'stock'

urlpatterns = [
    path('', show_market, name='show_market'),
    path('porto', show_stock, name='show_stock'),
    path('mjson/', show_market_json, name='show_market_json'),
    path('porto/njson/', show_note_json, name='show_note_json'),
    path('add/', add_stock, name='add_stock'),
    path('porto/add_note/', add_note, name='add_note'),
    path('delete_market/<int:market_id>', delete_market, name='delete_market'),
    path('delete_stock/<int:stock_id>', delete_stock, name='delete_stock'),
    path('json/', show_stock_json, name='show_stock_json'),
]
from django.urls import path
from stock.views import show_stock
app_name = 'stock'

urlpatterns = [
    path('', show_stock, name='show_stock'),
    #path('create_stock', create_stock, name='create_stock'),
]
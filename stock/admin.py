from django.contrib import admin
from stock.models import Saham, Pasar, Note

# Register your models here.
admin.site.register(Saham)
admin.site.register(Pasar)
admin.site.register(Note)

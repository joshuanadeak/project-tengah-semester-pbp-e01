from django.contrib import admin
from crypto.models import *

# Register your models here.
admin.site.register(Crypto)
admin.site.register(Market)
admin.site.register(Notes)
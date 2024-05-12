from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Venta)
admin.site.register(Detalle_venta)
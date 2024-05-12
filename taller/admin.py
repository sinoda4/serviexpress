from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Categoria_producto)
admin.site.register(Producto)

admin.site.register(Empleado)


from django.shortcuts import render, redirect
import json
from datetime import datetime, timedelta
from taller.models import *
from django.http import HttpResponse

# Create your views here.

def carrito(request):
    return render(request, "carrito/carrito.html", {})
    

def realizarCompra(request):
        
        data = request.POST.get("mi_dato")
        jdata = json.loads(data)
        
        


        username = None
        if request.user.is_authenticated:
            username = request.user
        
        venta = Venta.objects.create(
            FK_cliente = username,
            
        )

        

        #Se crea el detalle de la venta
        for j in jdata:
            print(j)
            vServicio = Producto.objects.get(pk=j['id'])
            Detalle_venta.objects.create(
                id_reserva = venta,
                Fk_producto = vServicio
            
        )
        return redirect("home")
        
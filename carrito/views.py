from django.shortcuts import render, redirect, get_object_or_404
import json
from datetime import datetime, timedelta
from taller.models import *
from django.http import HttpResponse, JsonResponse
from taller.models import Producto
from .carrito import Carrito


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
        

def add_carrito(request):
    carrito = Carrito(request)

    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto = get_object_or_404(Producto, pk=producto_id)

        carrito.add(producto=producto)

        return  JsonResponse({'Producto nombre': producto.nombre_producto})

def remove_carrito(request):
    print("hola")


from django.shortcuts import render, redirect, get_object_or_404
import json
from taller.models import *
from django.http import HttpResponse, JsonResponse
from taller.models import Producto
from .carrito import Carrito


# Create your views here.



def carrito(request):
    carrito = Carrito(request)
    productos_carrito = carrito.get_productos
    print(productos_carrito)

    return render(request, "carrito/carrito.html", {"productos_carrito": productos_carrito})
    

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
    #Obtener el carrito
    carrito = Carrito(request)

    if request.POST.get('action') == 'post':

        #Obtener el producto del carrito
        producto_id = int(request.POST.get('producto_id'))

        #Obtener el producto de la base de datos
        producto = get_object_or_404(Producto, pk=producto_id)

        #save session
        carrito.add(producto=producto)

        #add cantidad
        carrito_cantidad = carrito.__len__()



        #devolver si funciono o no
        return  JsonResponse({'Producto nombre': producto.nombre_producto})
        


def delete_carrito(request):
    pass

def update_carrito(request):
     pass

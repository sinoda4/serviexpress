from django.shortcuts import render, redirect, get_object_or_404
import json
from taller.models import *
from django.http import HttpResponse, JsonResponse
from taller.models import Producto
from .carrito import Carrito
import requests

# Create your views here.



def carrito(request):
    carrito = Carrito(request)
    productos_carrito = carrito.get_productos
    productos_cantidad = carrito.get_cantidad
    total_carrito = carrito.total

    return render(request, "carrito/carrito.html", {"productos_carrito": productos_carrito, "cantidades": productos_cantidad, "total": total_carrito})
    





def add_carrito(request):
    #Obtener el carrito
    carrito = Carrito(request)

    if request.POST.get('action') == 'post':

        #Obtener el producto del carrito
        producto_id = int(request.POST.get('producto_id'))
        producto_cantidad = int(request.POST.get('producto_cantidad'))

        #Obtener el producto de la base de datos
        producto = get_object_or_404(Producto, pk=producto_id)

        #save session
        carrito.add(producto=producto, cantidad=producto_cantidad)

        #add cantidad
        carrito_cantidad = carrito.__len__()



        #devolver si funciono o no
        return  JsonResponse({'Producto nombre': producto.nombre_producto})
        


def delete_carrito(request):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto = get_object_or_404(Producto, pk=producto_id)
        carrito.delete(producto)

        return JsonResponse({"Eliminado": producto.nombre_producto})

def update_carrito(request):
    carrito = Carrito(request)

    if request.POST.get('action') == 'post':

        #Obtener el producto del carrito
        producto_id = int(request.POST.get('producto_id'))
        producto_cantidad = int(request.POST.get('producto_cantidad'))
        producto = get_object_or_404(Producto, pk=producto_id)

        #Obtener el producto de la base de datos
        carrito.update(producto=producto, cantidad=producto_cantidad)

        return JsonResponse({"Cantidad": producto_cantidad})


    
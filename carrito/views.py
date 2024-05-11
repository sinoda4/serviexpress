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
    print(productos_carrito)

    return render(request, "carrito/carrito.html", {"productos_carrito": productos_carrito, "cantidades": productos_cantidad})
    

def realizarCompra(request):
        
        return redirect("home")
        



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
    pass

def update_carrito(request):
     pass


#Se utilizo payku como api
def payku(request):
    #KEY PUBLICA NO TOCAR, EN CASO DE NO FUNCIONAR HABLAR CON ADONIS
    PUBLIC_KEY = "tkpu412d0f80c14a55ff8bb7bb822247"
    BASE_URL = "https://app.payku.cl/api/transaction"
    if request.method == "POST":
        #DATA DE PRUEBA 
        data = {
            "email": "johndoe@example.com",
            "order": "98745",
            "subject": "payment description",
            "amount": 1,
            "payment": 1,
            "urlreturn": "https://localhost:8000",
            "urlnotify": "https://www.youwebsite.com/urlnotify?orderClient=98745",
            "additional_parameters": {
                "parameters1": "keyValue",
                "parameters2": "keyValue",
                "order_ext": "fff-777"
            }
        }


        url = BASE_URL  
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {PUBLIC_KEY}"
        }
        body = json.dumps(data)
        response = requests.post(url, headers=headers, data=body)

        if response.status_code == 200:
            result = response.json()
            
            """ print(result["url"])
            return redirect(result["url"]) """
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({'mal': 'mal'}, status=500)
                
    else:
        return render(request, 'carrito/transbank.html', {})
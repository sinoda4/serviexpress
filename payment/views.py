from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
import json
import requests

#Modelos
from carrito.carrito import Carrito
from payment.models import Venta, Detalle_venta
# Create your views here.

def payment(request):
    return render(request, "payments/payment_form.html", {})

def payment_succes(request):
    pass

def sumary(request):
    carrito = Carrito(request)
    productos_carrito = carrito.get_productos
    cantidades = carrito.get_cantidad
    total_carrito = carrito.total
    return render(request, "payments/payment_sumary.html", {"productos": productos_carrito, "cantidades": cantidades, "total_carrito": total_carrito})

def checkout(request):
    #Datos del carrito
    carrito = Carrito(request)
    productos_carrito = carrito.get_productos
    cantidades = carrito.get_cantidad
    total_carrito = carrito.total

    #Datos usuarios
    usuario = request.user

    #Mandar informacion de venta

    return render(request, "payments/payment_checkout.html", {"productos": productos_carrito, "cantidades": cantidades, "total_carrito": total_carrito, "usuario": usuario})


#REALIZAR VENTA Y PAGO CON PAYKU
def payment_process(request):
    #DATOS PAYKU
    PUBLIC_KEY = "tkpu412d0f80c14a55ff8bb7bb822247"
    BASE_URL = "https://app.payku.cl/api/transaction"

    if request.method == "POST":
        #Obtener datos del carrito
        carrito = Carrito(request)
        productos_carrito = carrito.get_productos
        productos_cantidades = carrito.get_cantidad
        


        
        #Obtener datos del usuario
        usuario = request.user

        #CREAR VENTA
        crear_venta = Venta(cliente=usuario)
        crear_venta.save()
        
        

        venta_id = crear_venta.pk
        #Obtener id de producto
        for p in productos_carrito():
            producto_id = p.pk

            for key, value in productos_cantidades().items():
                if int(key) == producto_id:
                    #CREAR DETALLE VENTA
                    crear_detalle_venta = Detalle_venta(venta=crear_venta,producto=p,cantidad=value)
                    crear_detalle_venta.save()
                    
        crear_venta.save()

        #REALIZAR PAGO CON PAYKU
        data = {
            "email": str(usuario.email),
            "order": str(venta_id),
            "subject": f"Pago de: {usuario.username} - orden: {venta_id}",
            "amount": int(crear_venta.total),
            "payment": 1,
            "urlreturn": "https://localhost:8000/home",
            "urlnotify": "https://localhost:8000/home",
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
            
            print(result["url"])
            return redirect(result["url"]) 
            #return JsonResponse(result, status=200)
        else:
            return JsonResponse({'mal': 'mal'}, status=500)
    
    else:
        pass


#ESTO ES UN EJEMPLO DE PRUEBA NO TOCAR 
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
    
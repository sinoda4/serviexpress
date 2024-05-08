from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .forms import *
import json
import requests
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["txtUsername"]
        password = request.POST["txtPassword"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Haz iniciado sesion correctamente"))
            return redirect('home')
        else:
            messages.error(request, ("Error de autentificacion, trate otra vez..."))
            return redirect('login')
    else:
        return render(request, "auth/inicioSesion.html", {})

def logout_user(request):
    logout(request)
    messages.warning(request, ("Haz cerrado sesion exitosamente"))
    return redirect('home')

#Registro de usuario
def register_user(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, ("Registro exitoso"))
            
            return redirect('home')
    else:
        form  = RegistroUsuarioForm()
        return render(request, 'auth/registroUsuario.html', {"form": form})


#Se utilizo payku como api
def transbank(request):
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
            "urlreturn": "https://youwebsite.com/urlreturn?orderClient=98745",
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
            print(result)
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({'mal': 'mal'}, status=500)
                
    else:
        return render(request, 'auth/transbank.html', {})
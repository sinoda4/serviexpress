from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .forms import *
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

def transbank(request):
    api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
    commerce_code = "597055555532"
    base_url = "https://webpay3gint.transbank.cl"
    if request.method == "POST":
        payload = {
            "buy_order": "ordenCompra12345678",
            "session_id": "sesion1234557545",
            "amount": 10000,
        }

        response = requests.post(f'{base_url}/rswebpaytransaction/api/webpay/v1.2/transactions/', json=payload, headers={'Tbk-Api-Key-Id': commerce_code, 'Tbk-Api-Key-Secret': api_key})
        if response.status_code == 200:
            data = response.json()
            print("funciona")
            return JsonResponse({'response': data})
        else:
            return JsonResponse({'error': 'Error en la solicitud a la API de Transbank'}, status=500)
        
        return redirect('transbank')
    else:
        return render(request, 'auth/transbank.html', {})
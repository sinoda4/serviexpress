from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
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
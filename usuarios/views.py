from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioCreacionUsuarios

def login(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            django_login(request,formulario.get_user())
            return redirect('home:home')
    return render(request,'usuarios/login.html',{'form':formulario})

def register(request):
    formulario = FormularioCreacionUsuarios()
    if request.method == 'POST':
        formulario = FormularioCreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
    return render(request,'usuarios/register.html',{'form':formulario})
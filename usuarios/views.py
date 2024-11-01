from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            username_in = formulario.cleaned_data.get('username')
            password_in = formulario.cleaned_data.get('password')
            credentials = authenticate(username=username_in,password=password_in)
            django_login(request,credentials)
            return redirect('home:home')
            
    return render(request,'usuarios/login.html',{'form':formulario})
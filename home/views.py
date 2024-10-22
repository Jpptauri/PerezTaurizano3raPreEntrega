from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from home.forms import CrearMascotaFormulario,BuscarMascotaFormulario
from home.models import Mascota

def home(request):
    return render(request,'index.html')

def about_me(request):
    return render(request,'about_me.html')

def buscar_mascotas(request):
    
    formulario = BuscarMascotaFormulario(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        especie = formulario.cleaned_data.get('especie')
        mascotas = Mascota.objects.filter(nombre__icontains=nombre,especie__icontains=especie)
        
    return render(request, 'buscar_mascotas.html',{'mascotas':mascotas,'form':formulario})

def crear_mascotas(request):
    formulario = CrearMascotaFormulario()
    if request.method == 'POST':
        formulario = CrearMascotaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre=data.get('nombre'),especie=data.get('especie'),edad=data.get('edad'))
            mascota.save()
            return redirect('home:buscar_mascotas')
        
    return render(request,'crear_mascotas.html',{'form':formulario})
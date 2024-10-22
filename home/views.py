from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from home.forms import CrearMascotaFormulario
from home.models import Mascota

def home(request):
    return render(request,'index.html')

def buscar_mascotas(request):
        return render(request, 'buscar_mascotas.html',{'mascota':''})

def crear_mascotas(request):
    formulario = CrearMascotaFormulario()
    if request.method == 'POST':
        formulario = CrearMascotaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre=data.get('nombre'),especie=data.get('especie'),edad=data.get('edad'))
            mascota.save()
    return render(request,'crear_mascotas.html',{'form':formulario})
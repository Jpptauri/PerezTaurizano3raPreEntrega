from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from home.forms import CrearMascotaFormulario,BuscarMascotaFormulario,EditarMascotaFormulario
from home.models import Mascota
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home/index.html')

def about_me(request):
    return render(request,'home/about_me.html')

def buscar_mascotas(request):
    
    formulario = BuscarMascotaFormulario(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        especie = formulario.cleaned_data.get('especie')
        mascotas = Mascota.objects.filter(nombre__icontains=nombre,especie__icontains=especie)
        
    return render(request, 'home/buscar_mascotas.html',{'mascotas':mascotas,'form':formulario})

@login_required
def crear_mascotas(request):
    formulario = CrearMascotaFormulario()
    if request.method == 'POST':
        formulario = CrearMascotaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre=data.get('nombre'),especie=data.get('especie'),edad=data.get('edad'))
            mascota.save()
            return redirect('home:buscar_mascotas')
        
    return render(request,'home/crear_mascotas.html',{'form':formulario})

@login_required
def ver_mascota(request,id):
    mascota = Mascota.objects.get(id=id)
    return render(request,'home/ver_mascota.html',{'mascota':mascota})
@login_required
def eliminar_mascota(request,id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('home:buscar_mascotas')
@login_required
def editar_mascota(request,id):
    mascota = Mascota.objects.get(id=id)
    formulario = EditarMascotaFormulario(initial={'nombre':mascota.nombre,'edad':mascota.edad,'especie':mascota.especie})
    
    if request.method == 'POST':
        formulario = EditarMascotaFormulario(request.POST) 
        if formulario.is_valid():
            mascota.nombre = formulario.cleaned_data.get('nombre')
            mascota.edad = formulario.cleaned_data.get('edad')
            mascota.especie = formulario.cleaned_data.get('especie')
            mascota.save()      
            return redirect('home:buscar_mascotas')
    return render(request,'home/editar_mascota.html',{'mascota':mascota,'form':formulario})
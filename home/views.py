from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def buscar_mascotas(request):
    return render(request,'buscar_mascotas.html')

def crear_mascotas(request):
    return render(request,'crear_mascotas.html')
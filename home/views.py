from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def buscar_perros(request):
    return render(request,'buscar_perros.html')

def crear_perros(request):
    return render(request,'crear_perros.html')
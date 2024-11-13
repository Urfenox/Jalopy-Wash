from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo

# Create your views here.

def index(request):
    return render(request, "cliente/index.html")

def agendar(request):
    return render(request, "cliente/agendar.html")

def buscar(request):
    patente = request.GET.get('patente', '')
    if patente:
        vehiculo = get_object_or_404(Vehiculo, patente=patente)
        return render(request, "cliente/buscar.html", {"vehiculo":vehiculo})
    return render(request, "cliente/buscar.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from cliente.models import Hora, Vehiculo

# Create your views here.

def index(request):
    return render(request, "administrador/index.html")

def horas(request):
    horas = Hora.objects.all().order_by("creado")
    patente = request.GET.get('cancelar', '')
    if patente:
        Hora.objects.get(patente=patente).delete()
        messages.warning(request, "¡Hora cancelada!")
        return redirect("administrador:horas")
    hora = request.GET.get('hora', '')
    if hora:
        hora = Hora.objects.get(patente=hora)
        hora.estado = request.GET.get('estado', '')
        hora.save(force_update=True)
        messages.success(request, "¡Hora actualizada!")
        return redirect("administrador:horas")
    return render(request, "administrador/horas.html", {"horas": horas})

def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "administrador/vehiculos.html", {"vehiculos": vehiculos})

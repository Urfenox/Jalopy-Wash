from django.shortcuts import render, redirect
from django.http import JsonResponse
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
    if request.POST:
        hora = Hora(dueño=request.POST.get('dueño', ''), patente=request.POST.get('patente', ''), estado=request.POST.get('estado', ''))
        hora.save()
        return JsonResponse({
            "estado": "OK",
            "datos": {
                "dueño": request.POST.get('dueño', ''),
                "patente": request.POST.get('patente', ''),
                "estado": request.POST.get('estado', '')
            }
        })
    return render(request, "administrador/horas.html", {"horas": horas})

def vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by("-entrada")
    patente = request.GET.get('eliminar', '')
    if patente:
        Vehiculo.objects.get(patente=patente).delete()
        messages.warning(request, "¡Vehiculo eliminado!")
        return redirect("administrador:vehiculos")
    vehiculo = request.GET.get('vehiculo', '')
    if vehiculo:
        vehiculo = Vehiculo.objects.get(patente=vehiculo)
        vehiculo.estado = request.GET.get('estado', '')
        vehiculo.save(force_update=True)
        messages.success(request, "¡Vehiculo actualizado!")
        return redirect("administrador:vehiculos")
    return render(request, "administrador/vehiculos.html", {"vehiculos": vehiculos})

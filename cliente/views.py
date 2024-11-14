from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Vehiculo, Hora
from .forms import Agendar

# Create your views here.

def index(request):
    return render(request, "cliente/index.html")

def agendar(request):
    form = Agendar(request.POST or None)
    if form.is_valid():
        hora_existente = Hora.objects.filter(patente=form.cleaned_data['patente'])
        if len(hora_existente) > 0:
            messages.error(request, "¡Ups! Ya existe una hora para este vehiculo.")
            response = redirect('cliente:agendar')
            response['Location'] += str(f'?patente={hora_existente[0].patente}')
            return response
        form.save()
        messages.success(request, "¡Hora agendada correctamente!")
        return redirect("cliente:agendar")
    patente = request.GET.get('patente', '')
    if patente:
        hora = get_object_or_404(Hora, patente=patente)
        if request.headers['content-type'] == "application/json":
            return JsonResponse({
                "dueño": hora.dueño,
                "patente": hora.patente,
                "estado": hora.estado,
                "creado": hora.creado
            })
        return render(request, "cliente/agendar.html", {"hora":hora})
    return render(request, "cliente/agendar.html", {"form": form})

def buscar(request):
    patente = request.GET.get('patente', '')
    if patente:
        vehiculo = get_object_or_404(Vehiculo, patente=patente)
        return render(request, "cliente/buscar.html", {"vehiculo":vehiculo})
    return render(request, "cliente/buscar.html")
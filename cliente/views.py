from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehiculo, Hora
from .forms import Agendar

# Create your views here.

def index(request):
    return render(request, "cliente/index.html")

def agendar(request):
    form = Agendar(request.POST or None)
    if form.is_valid():
        if Hora.objects.get(patente=form.cleaned_data['patente']):
            messages.error(request, "¡Ups! Ya existe una hora para este vehiculo.")
            return redirect("cliente:agendar")
        form.save()
        messages.success(request, "¡Hora agendada correctamente!")
        return redirect("cliente:agendar")
    return render(request, "cliente/agendar.html", {"form": form})

def buscar(request):
    patente = request.GET.get('patente', '')
    if patente:
        vehiculo = get_object_or_404(Vehiculo, patente=patente)
        return render(request, "cliente/buscar.html", {"vehiculo":vehiculo})
    return render(request, "cliente/buscar.html")
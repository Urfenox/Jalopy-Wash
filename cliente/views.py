from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "cliente/index.html")

def agendar(request):
    return render(request, "cliente/agendar.html")

def buscar(request):
    return render(request, "cliente/buscar.html")
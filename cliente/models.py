from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Vehiculo(models.Model):
    ESTADOS = {
        "ESPERA": "En espera...",
        "PREPARACION": "En preparación...",
        "LAVADO": "En lavado...",
        "SECADO": "En secado...",
        "LISTO": "Listo para retiro",
        "FINALIZADO": "Proceso terminado"
    }

    uid = models.PositiveSmallIntegerField()
    dueño = models.CharField(max_length=30) # rut ?
    patente = models.CharField(max_length=6)
    estado = models.CharField(max_length=12, choices=ESTADOS, default="ESPERA")
    entrada = models.DateTimeField(auto_now=False, auto_now_add=True)
    salida = models.DateTimeField(auto_now=True, auto_now_add=False)
    encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

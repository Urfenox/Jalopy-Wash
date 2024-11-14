from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Hora(models.Model):
    ESTADOS = {
        "ESPERA": "En espera...",
        "PENDIENTE": "Cercano a uso...",
        "USO": "En uso...",
        "FINALIZADO": "Terminado."
    }

    dueño = models.CharField(max_length=30)
    patente = models.CharField(max_length=6)
    estado = models.CharField(max_length=11, choices=ESTADOS, default="ESPERA")
    creado = models.DateTimeField(auto_now=False, auto_now_add=True)
    terminado = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.patente + " de " + self.dueño)

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
    dueño = models.CharField(max_length=30)
    patente = models.CharField(max_length=6)
    estado = models.CharField(max_length=12, choices=ESTADOS, default="ESPERA")
    entrada = models.DateTimeField(auto_now=False, auto_now_add=True)
    salida = models.DateTimeField(auto_now=True, auto_now_add=False)
    encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.patente + " de " + self.dueño)

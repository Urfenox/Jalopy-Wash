from django.urls import path
from .views import *

app_name = "administrador"

urlpatterns = [
    path('', index, name="index"),
    path('horas/', horas, name="horas"),
    path('vehiculos/', vehiculos, name="vehiculos"),
]
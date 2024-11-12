from django.urls import path
from .views import *

app_name = "cliente"

urlpatterns = [
    path('', index, name="index"),
    path('agendar/', agendar, name="agendar"),
    path('buscar/', buscar, name="buscar"),
]
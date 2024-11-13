from django import forms
from .models import Hora

class Agendar(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ["dueño", "patente"]
        widgets = {
            "dueño": forms.TextInput(attrs={"class": "form-control"}),
            "patente": forms.TextInput(attrs={"class": "form-control"})
        }
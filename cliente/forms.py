from django import forms
from .models import *

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields= [
            'nit',
            'nombre',
            'direccion',
        ]
        labels = {
            'nit': 'Nit',
            'nombre': 'Nombre',
            'direccion': 'Direccion'
        }
        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-contol'}),
            'nombre': forms.TextInput(attrs={'class': 'form-contol'}),
            'direccion': forms.TextInput(attrs={'class': 'form-contol'}),
        }

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields= [
            'cedula',
            'nombre',
            'direccion',
            'fecha_nacimiento'
        ]
        labels = {
            'cedula': 'Cedula',
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'fecha_nacimiento': 'Fecha de Nacimiento'
        }
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-contol'}),
            'nombre': forms.TextInput(attrs={'class': 'form-contol'}),
            'direccion': forms.TextInput(attrs={'class': 'form-contol'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-contol'}),
        }
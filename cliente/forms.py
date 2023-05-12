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
            'nit': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nit'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'direccion'}),
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
            'fecha_nacimiento': 'Fecha de Nacimiento (DD/MM/YYYY)'
        }
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'cedula'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'direccion'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'fecha_nacimiento'}),
        }
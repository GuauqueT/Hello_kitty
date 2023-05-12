from django import forms
from .models import *

class DecoradorForm (forms.ModelForm):
    class Meta:
        model=Decorador
        fields= [
            'codigo',
            'nombre',
            'salario',
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'salario': 'Salario'
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-contol'}),
            'nombre': forms.TextInput(attrs={'class': 'form-contol'}),
            'salario': forms.NumberInput(attrs={'class': 'form-contol'}),
        }
        
class PasteleroForm (forms.ModelForm):
    class Meta:
        model=Pastelero
        fields= [
            'codigo',
            'nombre',
            'salario',
            'pasaporte',
            'pais',
            'exp'
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'salario': 'Salario',
            'pasaporte': 'Pasaporte',
            'pais': 'País',
            'exp': 'Experiencia'
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-contol'}),
            'nombre': forms.TextInput(attrs={'class': 'form-contol'}),
            'salario': forms.NumberInput(attrs={'class': 'form-contol'}),
            'pasaporte': forms.TextInput(attrs={'class': 'form-contol'}),
            'pais': forms.TextInput(attrs={'class': 'form-contol'}),
            'exp': forms.TextInput(attrs={'class': 'form-contol'}),
        }
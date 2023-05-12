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
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Codigo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Nombre'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Salario'}),
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
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Codigo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Nombre'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Salario'}),
            'pasaporte': forms.TextInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Pasaportre'}),
            'pais': forms.TextInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'País'}),
            'exp': forms.TextInput(attrs={'class': 'form-control','id':'floatingImput', 'placeholder': 'Experiencia'}),
        }
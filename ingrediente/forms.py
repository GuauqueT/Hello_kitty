from django import forms
from .models import *

class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields= [
            'nombre',
            'unidad_medida',
        ]
        labels = {
            'nombre': 'Nombre de Ingrediente',
            'unidad_medida': 'Unidad de Medida',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nombre'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'unidad_medida'})
        }

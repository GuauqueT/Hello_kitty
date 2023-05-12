from django import forms
from .models import *

class PastelForm(forms.ModelForm):

    class Meta:
        model = Pastel
        fields= [
            'nombre',
            'ingrediente',
            'cantidad'
        ]
        labels = {
            'nombre': 'Nombre de Pastel',
            'ingrediente': 'Ingredientes',
            'cantidad': 'Cantiades (separados por -)'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nombre'}),
            'ingrediente': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline mt-4'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'cantidad'})
        }

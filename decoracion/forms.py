import datetime
from django import forms
from .models import *

class DecoracionForm(forms.ModelForm):

    class Meta:
        model = Decoracion
        fields= [
            'decorador',
            'hora_inicio',
            'hora_fin',
            'peso_final',
            'produccion'
        ]
        labels = {
            'decorador': 'Decorador',
            'hora_inicio': 'Hora de Incio',
            'hora_fin': 'Hora de Finalizaicon',
            'peso_final': 'Peso Final',
            'produccion': 'Produccion'
        }
        widgets = {
            'decorador': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'decorador'}),
            'hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'hora_incio', 'value': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'readonly': 'readonly'}),
            'hora_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'hora_fin', 'value': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}),
            'peso_final': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'horno'}),
            'produccion': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'produccion'}),
        }

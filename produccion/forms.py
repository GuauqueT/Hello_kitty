import datetime
from django import forms
from .models import *

class HornoForm(forms.ModelForm):

    class Meta:
        model = Horno
        fields= [
            'marca',
            'valor',
        ]
        labels = {
            'marca': 'Marca',
            'valor': 'Valor del Horno',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'marca'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'valor'}),
        }

class ProduccionForm(forms.ModelForm):

    class Meta:
        model = Produccion
        fields= [
            'temperatura',
            'hora_inicio',
            'hora_fin',
            'horno',
            'junta'
        ]
        labels = {
            'temperatura': 'Temperatura',
            'hora_inicio': 'Hora de Incio',
            'hora_fin': 'Hora de Finalizaicon',
            'horno': 'Horno usado',
            'junta': 'Pastelero'
        }
        widgets = {
            'temperatura': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'temperatura'}),
            'hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'hora_incio', 'value': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'readonly': 'readonly'}),
            'hora_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'hora_fin', 'value': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}),
            'horno': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'horno'}),
            'junta': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'junta'}),
        }

from django import forms
from .models import *
import datetime

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden
        fields= [
            'nombre',
            'tipo',
            'peso_min',
            'fecha_solicitud',
            'fecha_entrega',
            'observaciones',
            'empleado',
            'pastel',
            'precio'
        ]
        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo de Pastel',
            'peso_min': 'Peso Minimo',
            'fecha_solicitud': 'Fecha Solicitud',
            'fecha_entrega': 'Fecha de Entrega',
            'observaciones': 'Observaciones',
            'empleado': 'Empleado quien resive',
            'pastel': 'Pastel a ordenar',
            'precio': 'Precio Pastel'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'nombre'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'tipo'}),
            'peso_min': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'peso_min'}),
            'fecha_solicitud': forms.DateTimeInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'fecha_solicitud', 'value': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'readonly': 'readonly'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'fecha_entrega'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'observaciones'}),
            'empleado': forms.TextInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'empleado'}),    
            'pastel': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'pastel'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'precio'}),
            
        }

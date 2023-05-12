from django import forms
from .models import *

class JuntaForm(forms.ModelForm):

    class Meta:
        model = Junta
        fields= [
            'orden',
            'pastelero',
        ]
        labels = {
            'orden': 'Orden',
            'pastelero': 'Pastelero quien Elabora',
        }
        widgets = {
            'orden': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'orden'}),
            'pastelero': forms.Select(attrs={'class': 'form-control', 'id':'floatingInput', 'placeholder': 'pastelero'}),
        }

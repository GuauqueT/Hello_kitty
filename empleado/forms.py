from django import forms
from .models import *

class DecoradorForm (forms.ModelForm):
    class Meta:
        model=Decorador
        fields='__all__'
        
class PasteleroForm (forms.ModelForm):
    class Meta:
        model=Pastelero
        fields='__all__'
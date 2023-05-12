from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def empleado(request):
    pasteleros = Pastelero.objects.all()
    decoradores = Decorador.objects.all()
    return render(request, 'empleado.html', {'pasteleros': pasteleros, 'decoradores': decoradores})

def registro_decorador(request, type):
    if request.method == 'POST':
        if type == 'pastelero':
            form=PasteleroForm(request.POST)
        else:
            form=DecoradorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empleado:empleado')
    else:
        if type == 'pastelero':
            form=PasteleroForm
        else:
            form=DecoradorForm
        return render(request, 'form.html', {'form':form})
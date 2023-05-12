from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def cliente(request):
    empresas = Empresa.objects.all()
    personas = Persona.objects.all()
    return render(request, 'cliente.html', {'empresas': empresas, 'personas': personas})

def registro_cliente(request, type):
    if request.method == 'POST':
        if type == 'empresa':
            form=EmpresaForm(request.POST)
        else:
            form=PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cliente:cliente')
    else:
        if type == 'empresa':
            form=EmpresaForm
        else:
            form=PersonaForm
        return render(request, 'form.html', {'form':form})

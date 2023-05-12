
from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def ingrediente(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente.html', {'ingredientes': ingredientes})

def registro_ingrediente(request):
    if request.method == 'POST':
        form=IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ingrediente:ingrediente')
    else:
        form=IngredienteForm
        return render(request, 'form.html', {'form':form})
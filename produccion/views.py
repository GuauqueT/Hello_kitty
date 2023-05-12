
from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def produccion(request):
    hornos = Horno.objects.all()
    producciones = Produccion.objects.all()
    return render(request, 'produccion.html', {'producciones': producciones, 'hornos': hornos})

def registro_horno(request):
    if request.method == 'POST':
        form=HornoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('produccion:produccion')
    else:
        form=HornoForm
        return render(request, 'form.html', {'form':form})
    
def registro_produccion(request):
    if request.method == 'POST':
        form=ProduccionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('produccion:produccion')
    else:
        form=ProduccionForm
        return render(request, 'form.html', {'form':form})
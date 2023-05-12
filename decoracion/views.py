from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def decoracion(request):
    decoraciones = Decoracion.objects.all()
    return render(request, 'decoracion.html', {'decoraciones': decoraciones})

def registro_decoracion(request):
    if request.method == 'POST':
        form=DecoracionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('decoracion:decoracion')
    else:
        form=DecoracionForm
        return render(request, 'form.html', {'form':form})
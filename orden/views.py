
from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def orden(request):
    ordenes = Orden.objects.all()
    return render(request, 'orden.html', {'ordenes': ordenes})

def registro_orden(request):
    if request.method == 'POST':
        form=OrdenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('orden:orden')
    else:
        form=OrdenForm
        return render(request, 'form.html', {'form':form})
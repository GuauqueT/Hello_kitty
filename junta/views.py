
from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def junta(request):
    juntas = Junta.objects.all()
    return render(request, 'junta.html', {'juntas': juntas})

def registro_junta(request):
    if request.method == 'POST':
        form=JuntaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('junta:junta')
    else:
        form=JuntaForm
        return render(request, 'form.html', {'form':form})
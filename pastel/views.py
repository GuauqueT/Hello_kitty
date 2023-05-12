from django.shortcuts import render, redirect
from django.views import generic

from .forms import *
from .models import *
# Create your views here.
def pastel(request):
    pasteles = Pastel.objects.all()
    return render(request, 'pastel.html', {'pasteles': pasteles})

def registro_pastel(request):
    if request.method == 'POST':
        form=PastelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pastel:pastel')
    else:
        form=PastelForm
        return render(request, 'form.html', {'form':form})
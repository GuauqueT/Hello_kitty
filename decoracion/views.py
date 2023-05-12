from django.shortcuts import render
from django.views import generic

# Create your views here.
class decoracion(generic.TemplateView):
    template_name = 'decoracion.html'

from django.shortcuts import render
from django.views import generic

# Create your views here.
class ingrediente(generic.TemplateView):
    template_name = 'ingrediente.html'
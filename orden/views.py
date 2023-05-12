
from django.shortcuts import render
from django.views import generic

# Create your views here.
class orden(generic.TemplateView):
    template_name = 'orden.html'
from django.shortcuts import render
from django.views import generic
# Create your views here.
class cliente(generic.TemplateView):
    template_name = 'cliente.html'
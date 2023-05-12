
from django.shortcuts import render
from django.views import generic

# Create your views here.
class junta(generic.TemplateView):
    template_name = 'junta.html'
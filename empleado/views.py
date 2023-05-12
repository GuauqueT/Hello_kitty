from django.shortcuts import render
from django.views import generic
# Create your views here.
class empleado (generic.TemplateView):
    template_name='empleado.html'
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', produccion, name='produccion'),
    path('registro_horno/', registro_horno, name='registro_horno'),
    path('registro_produccion/', registro_produccion, name='registro_produccion'),
]

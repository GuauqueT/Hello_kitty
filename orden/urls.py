from django.urls import path, include
from .views import *

urlpatterns = [
    path('', orden, name='orden'),
    path('registro_orden/', registro_orden, name='registro_orden'),
]

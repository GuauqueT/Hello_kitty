from django.urls import path, include
from .views import *

urlpatterns = [
    path('', pastel, name='pastel'),
    path('registro_pastel/', registro_pastel, name='registro_pastel'),
]

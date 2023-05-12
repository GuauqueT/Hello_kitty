from django.urls import path, include
from .views import *

urlpatterns = [
    path('', junta, name='junta'),
    path('registro_junta', registro_junta, name='registro_junta'),
]

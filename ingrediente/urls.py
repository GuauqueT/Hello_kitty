from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ingrediente, name='ingrediente'),
    path('registro_ingrediente', registro_ingrediente, name='registro_ingrediente'),
]

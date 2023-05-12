from django.urls import path, include
from .views import *

urlpatterns = [
    path('', cliente, name='cliente'),
    path('registro_cliente/<str:type>', registro_cliente, name="registro_cliente")
]

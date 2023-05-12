from django.urls import path, include
from .views import *

urlpatterns = [
    path('', produccion.as_view(), name='produccion'),
]

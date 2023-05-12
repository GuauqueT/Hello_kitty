from django.urls import path, include
from .views import *

urlpatterns = [
    path('', empleado.as_view(), name='empleado'),
]

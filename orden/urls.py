from django.urls import path, include
from .views import *

urlpatterns = [
    path('', orden.as_view(), name='orden'),
]

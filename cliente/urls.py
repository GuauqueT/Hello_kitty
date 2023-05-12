from django.urls import path, include
from .views import *

urlpatterns = [
    path('', cliente.as_view(), name='cientes'),
]

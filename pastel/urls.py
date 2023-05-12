from django.urls import path, include
from .views import *

urlpatterns = [
    path('', pastel.as_view(), name='pastel'),
]

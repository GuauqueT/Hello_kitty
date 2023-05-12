from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ingrediente.as_view(), name='ingrediente'),
]

from django.urls import path, include
from .views import *

urlpatterns = [
    path('', junta.as_view(), name='junta'),
]

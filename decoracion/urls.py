from django.urls import path, include
from .views import *

urlpatterns = [
    path('', decoracion.as_view(), name='decoracion'),
]

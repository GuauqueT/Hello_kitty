from django.urls import path, include
from .views import *

urlpatterns = [
    path('', decoracion, name='decoracion'),
    path('registro_decoracion', registro_decoracion, name='registro_decoracion'),
]

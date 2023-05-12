from django.urls import path, include
from .views import *

urlpatterns = [
    path('', empleado, name='empleado'),
    path('registro_empleado/<str:type>', registro_decorador, name='registro_empleado')
]

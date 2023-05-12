from django.db import models

# Create your models here.
class Empresa(models.Model):
    nit=models.CharField(max_length=12, unique=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Empresas" 

class Persona(models.Model):
    cedula=models.CharField(max_length=12, unique=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    
    class Meta:
        verbose_name_plural="Personas" 
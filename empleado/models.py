from django.db import models

# Create your models here.
class Decorador (models.Model):
    nombre=models.CharField(max_length=50)
    salario=models.FloatField(max_length=10)
    codigo=models.IntegerField(unique=True)
    
class Pastelero (models.Model):
    nombre=models.CharField(max_length=50)
    salario=models.FloatField(max_length=10)
    codigo=models.IntegerField(unique=True)
    pasaporte=models.CharField(max_length=20, unique=True)
    pais=models.CharField(max_length=20)
    exp=models.CharField(max_length=10)
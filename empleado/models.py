from django.db import models

# Create your models here.
class Decorador (models.Model):
    nombre=models.CharField(max_length=50)
    salario=models.FloatField(max_length=10)
    codigo=models.IntegerField(max_length=20)
    
class Pastelero (models.Model):
    nombre=models.CharField(max_length=50)
    salario=models.FloatField(max_length=10)
    codigo=models.IntegerField(max_length=20)
    pasaporte=models.CharField(max_length=20)
    pais=models.CharField(max_length=20)
    exp=models.CharField(max_length=10)
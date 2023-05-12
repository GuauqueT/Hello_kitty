from django.db import models

from ingrediente.models import Ingrediente

# Create your models here.   
class Pastel (models.Model):
    nombre=models.CharField(max_length=50)
    ingrediente=models.ManyToManyField(Ingrediente,blank=False)
    cantidad=models.CharField(blank=False,max_length=100)
    
    class Meta:
        verbose_name_plural="Pasteles" 
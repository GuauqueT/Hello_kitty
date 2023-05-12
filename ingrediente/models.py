from django.db import models
# Create your models here.   
class Ingrediente (models.Model):
    nombre=models.CharField(max_length=50,unique=True)
    cantidad5=models.CharField(max_length=10,blank=False)

    
    class Meta:
        verbose_name_plural="Ingredientes" 
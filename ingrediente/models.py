from django.db import models
# Create your models here.   
class Ingrediente (models.Model):
    nombre=models.CharField(max_length=50,unique=True)
    unidad_medida=models.CharField(max_length=10,blank=False)

    def __str__(self) -> str:
        return f"{self.nombre}"
    class Meta:
        verbose_name_plural="Ingredientes" 
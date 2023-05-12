from django.db import models
from pastel.models import Pastel

# Create your models here.   
class Orden (models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50,null=False,blank=False)
    peso_min=models.FloatField(null=False)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)
    fecha_entrega=models.DateField(null=False)
    observaciones=models.CharField(max_length=200)
    empleado=models.CharField(max_length=50,blank=True)
    pastel_id=models.ForeignKey(Pastel,blank=False,null=False,on_delete=models.DO_NOTHING)

    cantidad=models.CharField(blank=False,max_length=100)
    
    class Meta:
        verbose_name_plural="Ordenes" 
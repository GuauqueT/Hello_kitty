from django.db import models
from pastel.models import Pastel

# Create your models here.   
class Orden (models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50,null=False,blank=False)
    peso_min=models.FloatField(null=False)
    fecha_solicitud=models.DateTimeField()
    fecha_entrega=models.DateField()
    observaciones=models.CharField(max_length=200, blank=True)
    empleado=models.CharField(max_length=50,blank=False)
    pastel=models.ForeignKey(Pastel,blank=False,null=False,on_delete=models.DO_NOTHING)
    precio=models.FloatField(null=False, default=1000)

    def __str__(self) -> str:
        return f"{self.nombre}"
    
    class Meta:
        verbose_name_plural="Ordenes" 
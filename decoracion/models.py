from django.db import models
from empleado.models import Decorador
from produccion.models import Produccion
# Create your models here.
class Decoracion(models.Model):
    decorador=models.ForeignKey(Decorador,blank=False,null=False,on_delete=models.DO_NOTHING)
    hora_inicio=models.DateTimeField()
    hora_fin=models.DateTimeField()
    peso_final=models.FloatField(null=False)
    produccion=models.ForeignKey(Produccion,blank=False,null=False,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
            return f"{self.junta}"
    class Meta:
        verbose_name_plural="Decoraciones"
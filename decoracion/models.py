from django.db import models
from empleado.models import Decorador
from produccion.models import Produccion
# Create your models here.
class Decoracion(models.Model):
    decorador_id=models.ForeignKey(Decorador,blank=False,null=False,on_delete=models.DO_NOTHING)
    hora_inicio=models.DateTimeField( auto_now_add=True)
    hora_fin=models.DateTimeField( auto_now_add=False)
    peso_final=models.FloatField(null=False)
    produccion_id=models.ForeignKey(Produccion,blank=False,null=False,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural="Decoraciones"
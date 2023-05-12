from django.db import models
from junta.models import Junta
# Create your models here.
class Horno(models.Model):
    marca=models.CharField(max_length=50)
    valor=models.FloatField(null=False)

    class Meta:
        verbose_name_plural="Hornos"

class Produccion(models.Model):
    temperatura=models.FloatField(null=False)
    hora_inicio=models.DateTimeField( auto_now_add=True)
    hora_fin=models.DateTimeField( auto_now_add=False)
    horno_id=models.ForeignKey(Horno,blank=False,null=False,on_delete=models.DO_NOTHING)
    junta_id=models.ForeignKey(Junta,blank=False,null=False,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural="Producciones"
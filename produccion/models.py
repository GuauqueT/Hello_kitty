from django.db import models
from junta.models import Junta
# Create your models here.
class Horno(models.Model):
    marca=models.CharField(max_length=50)
    valor=models.FloatField(null=False)

    def __str__(self) -> str:
        return f"{self.marca}"


    class Meta:
        verbose_name_plural="Hornos"

class Produccion(models.Model):
    temperatura=models.FloatField(null=False)
    hora_inicio=models.DateTimeField()
    hora_fin=models.DateTimeField()
    horno=models.ForeignKey(Horno,blank=False,null=False,on_delete=models.DO_NOTHING)
    junta=models.ForeignKey(Junta,blank=False,null=False,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
            return f"{self.junta}"

    class Meta:
        verbose_name_plural="Producciones"
from django.db import models
from orden.models import Orden
from empleado.models import Pastelero

# Create your models here.
class Junta(models.Model):
    orden=models.ForeignKey(Orden,blank=False,null=False,on_delete=models.DO_NOTHING)
    pastelero=models.ForeignKey(Pastelero,blank=False,null=False,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.pastelero}"

    class Meta:
        verbose_name_plural="Juntas" 
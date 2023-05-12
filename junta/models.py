from django.db import models
from orden.models import Orden
from empleado.models import Pastelero

# Create your models here.
class Junta(models.Model):
    orden_id=models.ForeignKey(Orden,blank=False,null=False,on_delete=models.DO_NOTHING)
    pastelero_id=models.ForeignKey(Pastelero,blank=False,null=False,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural="Juntas" 
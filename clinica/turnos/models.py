from django.db import models
from django.utils.timezone import now

# Create your models here.
class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    obra_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    edad = models.IntegerField()
    dni = models.BigIntegerField()
    telefono = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    # hora_consulta = models.TimeField(verbose_name="Hora de Consulta")
    fecha_consulta = models.DateField(verbose_name="Fecha de Consulta", default=now)
    fecha_create = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "turno"
        verbose_name_plural = "turnos"
    
    def __str__(self):
        return self.nombre

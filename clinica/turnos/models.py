from django.db import models

# Create your models here.
class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    obra_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    edad = models.IntegerField()
    dni = models.BigIntegerField()
    telefono = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    fecha_create = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

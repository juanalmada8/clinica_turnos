from django.db import models
from django.utils.html import format_html

# Create your models here.


class Especialidades(models.Model):
    
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_ESPECIALIDAD = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    ruta_imagen = models.FileField(upload_to='fotos/%Y/%m/%d', default='defecto/defecto.jpg', blank=True, null=True)
    estado = models.CharField(max_length=10,choices=APROBACION_ESPECIALIDAD, default='Borrador')

    def __str__(self):
        return ('<%s => %s: %s, %s>' % (self.__class__.__name__, self.nombre, self.descripcion, self.ruta_imagen))


    def tipo_de_especialidad(self):
        if self.estado == 'Retirado':
            return format_html('<span style="color: #f00;">{}</span>', self.estado, )
        elif self.estado == 'Borrador':
            return format_html('<span style="color: #f0f;">{}</span>', self.estado, )
        elif self.estado == 'Publicado':
            return format_html('<span style="color: #099;">{}</span>', self.estado, )
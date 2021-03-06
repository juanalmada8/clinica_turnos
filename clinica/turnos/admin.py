from django.contrib import admin
from turnos.models import Turno


class TurnoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'obra_social', 'email', 'edad', 'dni', 'telefono', 'direccion','fecha_consulta']
    list_display = ['nombre', 'obra_social', 'fecha_consulta','email', 'edad','telefono','direccion','fecha_create','fecha_update']
    ordering = ['-nombre']
    list_filter = ('nombre', 'obra_social')


admin.site.register(Turno, TurnoAdmin)




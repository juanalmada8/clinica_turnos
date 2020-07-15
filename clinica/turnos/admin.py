from django.contrib import admin
from turnos.models import Turno,HoraConsulta, FechaConsulta


class TurnoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'obra_social', 'email', 'edad', 'dni', 'telefono', 'direccion']
    list_display = ['nombre', 'obra_social', 'email', 'edad','telefono','direccion','fecha_create','fecha_update']
    ordering = ['-nombre']
    list_filter = ('nombre', 'obra_social')

class FechaConsultaAdmin(admin.ModelAdmin):
    fields = ['fecha_consulta']
    list_display = ['fecha_consulta']


class HoraConsultaAdmin(admin.ModelAdmin):
    fields = ['hora']
    list_display = ['hora','fecha_consulta']

admin.site.register(Turno, TurnoAdmin)
admin.site.register(FechaConsulta,FechaConsultaAdmin)
admin.site.register(HoraConsulta,HoraConsultaAdmin)




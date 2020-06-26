from django.contrib import admin
from servicios.models import Especialidades


def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

class EspecialidadesAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion', 'ruta_imagen']
    list_display = ['nombre', 'descripcion', 'ruta_imagen', 'tipo_de_especialidad',]
    ordering = ['-descripcion']
    list_filter = ('nombre', 'descripcion',)
    actions = [publicar] 

admin.site.register(Especialidades, EspecialidadesAdmin)



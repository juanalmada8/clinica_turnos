from django.contrib import admin
from about.models import About
# Register your models here.


def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

class AboutAdmin(admin.ModelAdmin):
    fields = ['titulo', 'subtitulo', 'descripcion', 'ruta_imagen']
    list_display = ['titulo', 'subtitulo', 'ruta_imagen', 'fecha_create','fecha_update']
    ordering = ['-titulo']
    list_filter = ('titulo', 'subtitulo','fecha_create','fecha_update')
    actions = [publicar] 

admin.site.register(About, AboutAdmin)
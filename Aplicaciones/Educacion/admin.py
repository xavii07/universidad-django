from django.contrib import admin
from .models import Carrera,Curso, Materia

# Register your models here.
#admin.site.register(Carrera)
#admin.site.register(Curso)
#admin.site.register(Materia)

@admin.register(Carrera)
class CarrerasAdmin(admin.ModelAdmin):
    list_display=('id_car','nombre_car', 'fecha_creacion_car', 'telefono_car')
    ordering=('nombre_car','telefono_car')
    search_fields=('nombre_car',)
    #list_editable=('nombre_car',)
    list_filter=('nombre_car','fecha_creacion_car')
    list_per_page=5
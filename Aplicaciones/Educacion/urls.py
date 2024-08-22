from django.urls import path
from .views import carrera_views, curso_views


urlpatterns = [
    #Carrera
    path('', carrera_views.inicio),
    path('carreras/', carrera_views.carreras, name="carreras"),
    path('crear_carrera/', carrera_views.crear_carrera, name="crear_carrera"),
    path('eliminar_carrera/<id>', carrera_views.eliminar_carrera, name="eliminar_carrera"),
    path('editar_carrera/<id>', carrera_views.editar_carrera, name="editar_carrera"),
    path('procesar_editar_carrera/', carrera_views.procesar_editar_carrera, name="procesar_editar_carrera"),
    #Curso
    path('cursos/', curso_views.cursos, name="cursos"),
    path('crear_curso/', curso_views.crear_curso, name="crear_curso"),
    path('eliminar_curso/<id>', curso_views.eliminar_curso, name="eliminar_curso"),
    path('editar_curso/<id>', curso_views.editar_curso, name="editar_curso"),
    path('procesar_editar_curso/', curso_views.procesar_editar_curso, name="procesar_editar_curso"),
]
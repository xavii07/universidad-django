from django.urls import path
from .views import carrera_views, curso_views, materia_views, correo_views


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
    #Materias
    path('materias/', materia_views.materias, name="materias"),
    path('crear_materia/', materia_views.crear_materia, name="crear_materia"),
    path('eliminar_materia/<id>', materia_views.eliminar_materia, name="eliminar_materia"),
    path('editar_materia/<id>', materia_views.editar_materia, name="editar_materia"),
    path('procesar_editar_materia/', materia_views.procesar_editar_materia, name="procesar_editar_materia"),
    #Correo
    path('correo/', correo_views.correo, name="correo"),
    path('enviar_correo/', correo_views.enviar_correo, name="enviar_correo"),
]
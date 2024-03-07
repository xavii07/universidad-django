from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('carreras/', views.carreras, name="carreras"),
    path('crear_carrera/', views.crear_carrera, name="crear_carrera"),
    path('eliminar_carrera/<id>', views.eliminar_carrera, name="eliminar_carrera"),
    path('editar_carrera/<id>', views.editar_carrera, name="editar_carrera"),
]
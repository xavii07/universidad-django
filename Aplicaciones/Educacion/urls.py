from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('carreras/', views.carreras, name="carreras"),
    path('crear_carrera/', views.crear_carrera, name="crear_carrera"),
]
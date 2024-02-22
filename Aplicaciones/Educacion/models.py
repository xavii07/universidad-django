from django.db import models

# Create your models here.
class Carrera(models.Model):
    id_car=models.AutoField(primary_key=True)
    nombre_car=models.CharField(max_length=50)
    fecha_creacion_car=models.DateField()
    telefono_car=models.CharField(max_length=10)
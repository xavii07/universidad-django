from django.shortcuts import render, redirect
from .models import Carrera

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def carreras(request):

    carrerasDbb = Carrera.objects.all()

    return render(request, 'carreras.html', {
        "carreras": carrerasDbb
    })

def crear_carrera(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_car']
        fecha_creacion = request.POST['fecha_creacion_car']
        telefono = request.POST['telefono_car']

        Carrera.objects.create(nombre_car=nombre, fecha_creacion_car=fecha_creacion, telefono_car=telefono)
        return redirect('/carreras')
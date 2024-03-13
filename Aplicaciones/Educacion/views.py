from django.shortcuts import render, redirect
from .models import Carrera
from django.contrib import messages

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
        messages.success(request, 'Carrera creada correctamente')
        return redirect('/carreras')

def eliminar_carrera(request, id):
    carreraDb = Carrera.objects.get(id_car=id)

    carreraDb.delete()
    messages.success(request, 'Carrera borrada de la base de datos')
    return redirect('/carreras')

def editar_carrera(request, id):
    carreraDb = Carrera.objects.get(id_car=id)

    return render(request, 'editar_carrera.html', {
      "carrera": carreraDb
    })

def procesar_editar_carrera(request):
    if request.method == 'POST':
        id = request.POST['id_car']
        nombre = request.POST['nombre_car']
        fecha_creacion = request.POST['fecha_creacion_car']
        telefono = request.POST['telefono_car']

        carrera_editar = Carrera.objects.get(id_car=id)
        carrera_editar.nombre_car = nombre
        carrera_editar.fecha_creacion_car = fecha_creacion
        carrera_editar.telefono_car = telefono
        carrera_editar.save()

        messages.success(request, 'Carrera actualizada correctamente')
        return redirect('/carreras')
from django.shortcuts import render, redirect
from ..models import Carrera, Curso
from django.contrib import messages

def cursos(request):

    cursosDbb = Curso.objects.all()
    carrerasDbb = Carrera.objects.all()

    return render(request, 'cursos/cursos.html', {
        "cursos": cursosDbb,
        "carreras": carrerasDbb
    })

def crear_curso(request):
    if request.method == 'POST':
        nivel = request.POST['nivel_cur']
        aula = request.POST['aula_cur']
        fk_id_car = request.POST['fk_id_car']

        carrera_selec = Carrera.objects.get(id_car=fk_id_car)
        Curso.objects.create(nivel_cur=nivel, aula_cur=aula, fk_id_car=carrera_selec)
        messages.success(request, 'Curso creado correctamente')
        return redirect('/cursos')

def eliminar_curso(request, id):
    cursoDbb = Curso.objects.get(id_cur=id)

    cursoDbb.delete()
    messages.success(request, 'Curso borrado de la base de datos')
    return redirect('/curso')

def editar_curso(request, id):
    cursoDbb = Curso.objects.get(id_cur=id)
    carrerasDbb = Carrera.objects.all()

    return redirect(request, 'cursos/editar_curso.html', {
        "curso": cursoDbb,
        "carreras": carrerasDbb
    })

def procesar_editar_curso(request):
    if request.method == 'POST':
        id_cur = request.POST['id_cur']
        nivel = request.POST['nivel_cur']
        aula = request.POST['aula_cur']
        fk_id_car = request.POST['fk_id_car']

        carrera_selec = Carrera.objects.get(id_car=fk_id_car)
        curso_editar = Curso.objects.get(id_cur=id_cur)
        curso_editar.nivel_cur = nivel
        curso_editar.aula_cur = aula
        curso_editar.fk_id_car = carrera_selec
        curso_editar.save()

        messages.success(request, 'Curso actualizado correctamente')
        return redirect('/cursos')
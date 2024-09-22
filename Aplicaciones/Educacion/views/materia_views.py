from django.shortcuts import render, redirect
from ..models import  Curso, Materia
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def materias(request):

    cursosDbb = Curso.objects.all()
    materiasDbb = Materia.objects.all()

    return render(request, 'materias/materias.html', {
        "cursos": cursosDbb,
        "materias": materiasDbb
    })

@login_required(login_url='/login/')
def crear_materia(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_mat']
        creditos = request.POST['creditos_mat']
        silabo = request.FILES.get('silabo_mat')
        fk_id_cur = request.POST['fk_id_cur']

        curso_selec = Curso.objects.get(id_cur=fk_id_cur)
        Materia.objects.create(nombre_mat=nombre, creditos_mat=creditos, silabo_mat=silabo, fk_id_cur=curso_selec)
        messages.success(request, 'Materia creada correctamente')
        return redirect('/materias')

@login_required(login_url='/login/')
def eliminar_materia(request, id):
    materiaDbb = Materia.objects.get(id_mat=id)

    materiaDbb.delete()
    messages.success(request, 'Materia borrado de la base de datos')
    return redirect('/materias')

@login_required(login_url='/login/')
def editar_materia(request, id):
    materiaDbb = Materia.objects.get(id_mat=id)
    cursosDbb = Curso.objects.all()

    return render(request, 'materias/editar_materia.html', {
        "materia": materiaDbb,
        "cursos": cursosDbb
    })

@login_required(login_url='/login/')
def procesar_editar_materia(request):
    if request.method == 'POST':
        id_mat = request.POST['id_mat']
        nombre = request.POST['nombre_mat']
        creditos = request.POST['creditos_mat']
        silabo = request.FILES.get('silabo_mat')
        fk_id_cur = request.POST['fk_id_cur']

        curso_selec = Curso.objects.get(id_cur=fk_id_cur)
        materia_editar = Materia.objects.get(id_mat=id_mat)
        materia_editar.nombre_mat = nombre
        materia_editar.creditos_mat = creditos
        materia_editar.fk_id_car = curso_selec
        if silabo is not None:
            materia_editar.silabo_mat = silabo
        materia_editar.save()

        messages.success(request, 'Materia actualizado correctamente')
        return redirect('/materias')
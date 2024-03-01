from django.shortcuts import render
from .models import Carrera

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def carreras(request):

    carrerasDbb = Carrera.objects.all()

    return render(request, 'carreras.html', {
        "carreras": carrerasDbb
    })
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def correo(request):
    return render(request, 'correo/correo.html')

def enviar_correo(request):
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        try:
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario], fail_silently=False)
            messages.success(request, 'Mensaje enviado correctamente')

        except Exception as e:
            messages.error(request, f'No se pudo enviar el mensaje {e}')

    return redirect('/correo')


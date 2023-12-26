from django.shortcuts import render
from django.core.mail import send_mail
from .models import Notificacion, Usuario


def enviar_notificacion(request, notificacion_id, usuario_id):
    notificacion = Notificacion.objects.get(id=notificacion_id)
    usuario = Usuario.objects.get(id=usuario_id)

    # Enviar correo electrónico
    send_mail(
        'Notificacion Teravision',
        notificacion.mensaje,
        'jjusturi@gmail.com',  # Remitente
        ['jjusturi@gmail.com'],  # Destinatario
        fail_silently=False,
    )

    return render(request, 'notificaciones/notificacion_enviada.html', {'usuario': usuario})


def ver_notificaciones(request):
        notificaciones = Notificacion.objects.all()
        return render(request, 'notificaciones/ver_notificaciones.html', {'notificaciones': notificaciones})

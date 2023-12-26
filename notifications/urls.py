# notificaciones/urls.py
from django.urls import path
from .views import enviar_notificacion, ver_notificaciones

urlpatterns = [
    path('enviar_notificacion/<int:notificacion_id>/<int:usuario_id>/', enviar_notificacion, name='enviar_notificacion'),
    path('ver_notificaciones/', ver_notificaciones, name='ver_notificaciones'),
    # Otras URL...
]

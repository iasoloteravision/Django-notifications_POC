# notificaciones/admin.py
from django.contrib import admin
from .models import Notificacion, Usuario

admin.site.register(Notificacion)
admin.site.register(Usuario)

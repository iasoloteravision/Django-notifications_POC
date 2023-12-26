from django.db import models


class Notificacion(models.Model):
    mensaje = models.TextField()


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

from django.db import models

# Create your models here.
class Contactanos(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    telefono = models.CharField(max_length = 25)
    correo = models.CharField(max_length = 75)
    comentario = models.CharField(max_length = 600)
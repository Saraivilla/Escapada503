from django.db import models

# Create your models here.
class Guias(models.Model):
    nombre = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 600)
    correo = models.CharField(max_length = 75)
    telefono = models.CharField(max_length = 25)
    zona = models.CharField(max_length = 75)  
    fotografia = models.CharField(max_length = 75)
    
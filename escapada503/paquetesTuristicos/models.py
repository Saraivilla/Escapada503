from django.db import models
from guiasTuristicos.models import Guias
from django.contrib.auth.models import User

# Create your models here.
class Paquetes(models.Model):
    nombre = models.CharField(max_length = 255)
    ubicacion = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 800)
    fecha = models.CharField(max_length = 100)
    salida = models.CharField(max_length = 100)
    regreso = models.CharField(max_length = 100)
    incluye = models.CharField(max_length = 255)
    gastosExtra = models.CharField(max_length = 300)
    recorrido = models.CharField(max_length = 255)
    precio = models.CharField(max_length = 60)
    guiaEncargado = models.ForeignKey(Guias, on_delete = models.CASCADE)
    imagenes = models.CharField(max_length = 75)

    def guia_nombre(self):
        return self.guiaEncargado.nombre  

    guia_nombre.short_description = 'guiaEncargado'


class Reservas(models.Model):
    usuarioReserva = models.ForeignKey(User, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Paquetes, on_delete=models.CASCADE)
    cantidadPersonas = models.IntegerField()
    total = models.FloatField()

    def lugar_nombre(self):
        return self.lugar.nombre  

    lugar_nombre.short_description = 'Lugar'

    
    
    


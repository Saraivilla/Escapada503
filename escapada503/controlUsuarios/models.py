from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DatosUsuarios(models.Model):
    datosUsuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(max_length = 25)
    dui = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.datosUsuario.username
    
    def usuario_nombre(self):
        return f"{self.datosUsuario.first_name} {self.datosUsuario.last_name}"
    
    usuario_nombre.short_description = "datosUsuario"
from django.contrib import admin
from .models import User, DatosUsuarios

# Register your models here.
@admin.register(DatosUsuarios)
class DatosUsuariosModelAdmin(admin.ModelAdmin):
    list_display = [ 'usuario_nombre', 'telefono', 'dui']    
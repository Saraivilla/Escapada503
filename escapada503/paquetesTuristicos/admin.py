from django.contrib import admin
from .models import Paquetes, Reservas

# Register your models here.
@admin.register(Paquetes)
class ContactanosModelAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'ubicacion','descripcion', 'fecha','salida', 'regreso', 'incluye', 'gastosExtra','recorrido','precio','guia_nombre']


@admin.register(Reservas)
class ReservasModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuarioReserva', 'lugar_nombre', 'cantidadPersonas', 'total']    
from django.contrib import admin
from .models import Contactanos

# Register your models here.
@admin.register(Contactanos)
class ContactanosModelAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'apellido','telefono', 'correo','comentario']
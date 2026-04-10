from django.contrib import admin
from .models import Guias


# Register your models here.
@admin.register(Guias)
class GuiasModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'correo', 'telefono', 'zona', 'fotografia']    
from django.urls import path
from django.contrib.auth import views as auth_views  # Asegúrate de que esta línea esté presente

from . import views

urlpatterns = [
     path('registro/', views.registro, name='registro'),
     path('perfil/', views.perfil, name='perfil'),
     path('cambioContraseña/', views.contraseña, name='cambioContraseña'),     
     path('reservas/', views.mostrarReservas, name="reservas"),
]

from django.urls import path
from paquetesTuristicos import views

urlpatterns = [
    path('', views.paquetes, name = "paquetes-url"),
]
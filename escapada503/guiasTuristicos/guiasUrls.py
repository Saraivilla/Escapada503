from django.urls import path
from guiasTuristicos import views

urlpatterns = [
    path('', views.guias, name = "guias-url"),

]
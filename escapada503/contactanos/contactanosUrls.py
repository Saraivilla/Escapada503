
from django.urls import path
from contactanos import views

urlpatterns = [
    path('', views.contactanos, name = "contactanos-url"),

]

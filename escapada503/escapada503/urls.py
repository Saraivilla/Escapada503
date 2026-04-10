from django.contrib import admin
from django.urls import path, include
from controlUsuarios import views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.indexUrls')),
    path('contacto/', include('contactanos.contactanosUrls')),
    path('guias/', include('guiasTuristicos.guiasUrls')),
    path('paquetes/', include('paquetesTuristicos.paquetesUrls')),
    path('blog/', include('blog.blogUrls')),
    path('nosotros/', include('nosotros.nosotrosUrls')),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('cambioContraseña/', views.contraseña, name='cambioContraseña'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('reservas/', views.mostrarReservas, name="reservas"),
    #Cambio de contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistroForm 
from .forms import DatosPersonalesForm, UsuariosForm
from .models import DatosUsuarios
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from paquetesTuristicos.models import Reservas

# Create your views here.

#----LOGIN----
@login_required(login_url = '/account/login/')
def inicio(request):
    return render()

@login_required   
def contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantener la sesión del usuario
            return redirect('login')  # Redirigir a la página de perfil u otra página después del cambio de contraseña
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'cambioContraseña.html', {'form': form})

# REGISTRAR UN NUEVO USUARIO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirigir a la página principal después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registrarUsuario.html', {'form': form})


# Mostrar Perfil

@login_required
def perfil(request):
    usuario = request.user
    usuario_instance, created = DatosUsuarios.objects.get_or_create(datosUsuario=usuario)
    
    if request.method == 'POST':
        # Procesar ambos formularios cuando se envíe el formulario
        formUser = DatosPersonalesForm(request.POST, instance=usuario)
        formUsuarios = UsuariosForm(request.POST, instance=usuario_instance)
        
        if formUser.is_valid() and formUsuarios.is_valid():
            formUser.save()
            formUsuarios.save()
            return redirect('perfil')  # Redirigir a la misma página para evitar reenvíos de formulario
    else:
        # Cargar formularios con las instancias existentes
        formUser = DatosPersonalesForm(instance=usuario)
        formUsuarios = UsuariosForm(instance=usuario_instance)
    
    context = {
        'formUser': formUser,
        'formUsuarios': formUsuarios,
    }
    return render(request, 'perfilUsuario.html', context) 

#RESERVAS
@login_required
def mostrarReservas(request):
    reservaLista = Reservas.objects.filter(usuarioReserva=request.user)
    return render(request, 'reservas.html',{'reservaLista':reservaLista})
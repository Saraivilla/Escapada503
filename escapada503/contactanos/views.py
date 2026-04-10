from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactoForm
from controlUsuarios.models import DatosUsuarios

@login_required
def contactanos(request):
    user = request.user
    try:
        datos_usuarios = DatosUsuarios.objects.get(datosUsuario=user)
    except DatosUsuarios.DoesNotExist:
        datos_usuarios = None

    if request.method == 'POST':
        form = ContactoForm(request.POST, user=user, datos_usuarios=datos_usuarios)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Reemplaza 'success_url' con la URL adecuada para redireccionar tras el éxito
    else:
        form = ContactoForm(user=user, datos_usuarios=datos_usuarios)

    return render(request, 'contactanos.html', {'form': form})

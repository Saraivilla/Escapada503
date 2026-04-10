from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    nombre_usuario = request.user.username
    print(nombre_usuario)  # Agrega esta línea para verificar
    contexto = {
        'nombre_usuario': nombre_usuario
    }
    return render(request, "index.html", contexto)

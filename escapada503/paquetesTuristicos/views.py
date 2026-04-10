from django.shortcuts import render, redirect
from .models import Paquetes, Reservas
from django.contrib.auth.decorators import login_required

@login_required
def paquetes(request):
    paquetesLista = Paquetes.objects.all()
    
    if request.method == 'POST':
        paquete_id = request.POST.get('paquete_id')
        cantidadPersonas = request.POST.get('cantidad')
        total = request.POST.get('total')
        usuarioReserva = request.user

        # Obtén el paquete desde el ID
        paquete = Paquetes.objects.get(id=paquete_id)
        
        # Crea y guarda la reserva
        reserva = Reservas(
            usuarioReserva=usuarioReserva,
            lugar=paquete,
            cantidadPersonas=int(cantidadPersonas),
            total = total
        )
        reserva.save()
        
        return redirect('paquetes-url')  # Redirige a una página de éxito

    return render(request, 'paquetes.html', {'paquetesLista': paquetesLista})

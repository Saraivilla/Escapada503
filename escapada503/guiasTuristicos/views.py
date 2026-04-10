from django.shortcuts import render
from .models import Guias
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def guias(request):
    guiasLista = Guias.objects.all()
    return render(request, 'guias.html', {'guiasLista' : guiasLista})
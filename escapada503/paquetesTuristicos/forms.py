from django import forms
from .models import Reservas

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['usuarioReserva', 'lugar', 'cantidadPersonas'] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtener el usuario autenticado desde la vista
        super().__init__(*args, **kwargs)
        if user:
            self.fields['usuarioReserva'].initial = user.id  # Establecer el valor inicial del campo user con el ID del usuario


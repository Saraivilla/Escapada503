# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DatosUsuarios
from paquetesTuristicos.models import Reservas

#REGISTRAR UN NUEVO USUARIO (TABLA AUTH_USER)
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    username = forms.CharField(label="Usuario")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        error_messages = {
            'username': {
                'unique': "Este nombre de usuario ya está en uso.",
            },
            'email': {
                'unique': "Este correo electrónico ya está en uso.",
            },
            'password1': {
                'required': "La contraseña es obligatoria.",
            },
            'password2': {
                'required': "La confirmación de la contraseña es obligatoria.",
                'password_mismatch': "Las contraseñas no coinciden.",
            },
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email


# Formulario para mostrar datos de perfil (tabla auth_user)
class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = DatosUsuarios
        fields = ['telefono', 'dui']  # Incluye todos los campos adicionales aquí

    def __init__(self, *args, **kwargs):
        super(UsuariosForm, self).__init__(*args, **kwargs)
        self.fields['telefono'].required = False
        self.fields['dui'].required = False

#RESERVAS
class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['usuarioReserva', 'lugar', 'cantidadPersonas', 'total']

from django import forms
from django import forms
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm

class CustomPasswordChangeForm(AuthPasswordChangeForm):
    old_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='La nueva contraseña debe tener al menos 8 caracteres.'
    )
    new_password2 = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



from django import forms
from django.contrib.auth.models import User
from controlUsuarios.models import DatosUsuarios
from .models import Contactanos

class ContactoForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(label='Apellido', max_length=50, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(label='Correo Electrónico')
    telefono = forms.CharField(label='Teléfono', required=False)
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea, required=True)

    class Meta:
        model = Contactanos
        fields = ['comentario']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        datos_usuarios = kwargs.pop('datos_usuarios', None)
        super(ContactoForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
        
        if datos_usuarios:
            self.fields['telefono'].initial = datos_usuarios.telefono

    def save(self, commit=True):
        contactanos = super(ContactoForm, self).save(commit=False)
        contactanos.nombre = self.cleaned_data['first_name']
        contactanos.apellido = self.cleaned_data['last_name']
        contactanos.correo = self.cleaned_data['email']
        contactanos.telefono = self.cleaned_data['telefono']
        
        if commit:
            contactanos.save()
        return contactanos

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    campos = (
        ('administrador', 'admin'),
        ('usuario comun', 'usuario_comun'),
        ('moderador','moderador')
    )
    email = forms.EmailField(required=False)
    tipo_usuario = forms.ChoiceField(choices=campos)
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'tipo_usuario']

class ActualizarUsuarioForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']
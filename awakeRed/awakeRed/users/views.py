from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm, ActualizarPerfilForm, ActualizarUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            print(username)
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save()
            return redirect('blog-home')
        else:
            messages.error(request, "Hubo un error en el registro")
    formulario = RegistroUsuarioForm()
    return render(request, 'users/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    if request.method == "POST":
        formulario_usuario = ActualizarUsuarioForm(request.POST,instance= request.user)
        formulario_perfil = ActualizarPerfilForm(request.POST, request.FILES, instance= request.user.perfil)
        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            formulario_usuario.save()
            formulario_perfil.save()
            return redirect('perfil')
    else:
        formulario_usuario = ActualizarUsuarioForm(instance= request.user)
        formulario_perfil = ActualizarPerfilForm(instance= request.user.perfil)
    contexto = {
        'formulario_usuario': formulario_usuario,
        'formulario_perfil' : formulario_perfil
    }

    return render(request, 'users/perfil.html', contexto)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
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
    return render(request, 'users/perfil.html')
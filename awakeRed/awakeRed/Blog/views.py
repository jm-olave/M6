from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
from .forms import TweetForm, ContactoForm, ComentarioForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    contexto ={
        'publicacionesLlave' : Publicacion.objects.raw('SELECT * FROM Blog_publicacion ORDER BY id DESC'),
        'titulo': 'Blog-Landing'
    }
    return render(request,'Blog/index.html', contexto)

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            texto = formulario.cleaned_data['texto']
            check = formulario.cleaned_data['check']
            mensaje_alerta = f'Texto enviado: {texto} checkeo politicas: {check}'
            messages.success(request, mensaje_alerta)

            print(mensaje_alerta)
    formulario_c  = ContactoForm()
    contexto = {
        'titulo': "Contacto",
        'formulario': formulario_c
        }
    return render(request, 'Blog/contacto.html', contexto)


# formularios

def createTweet(request):
    if request.method == "POST":
        formulario_post = TweetForm(request.POST)
        if formulario_post.is_valid():
            tweet = formulario_post.save(commit=False)
            tweet.save()
            
    formulario_get = TweetForm()
    return render(request, "Blog/tweet_create.html",{'formulario': formulario_get})

def crear_comentario(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk=publicacion_id)
    if request.method == "POST":
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.usuario = request.user
            comentario.publicacion = publicacion
            comentario.save()
    else:
        formulario = ComentarioForm()
    return render(request, 'Blog/crear_comentario.html', {'formulario': formulario})


# Vistas Genericas

# DETALLE publicacion
class PublicacionDetailView(DetailView):
    model = Publicacion
      #<app>/<model>_<viewtype>.html

# CREAR publicacion
class PublicacionCreateView(CreateView):
    model = Publicacion
    fields = ['titulo','contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# EDITAR publicacion
class PublicacionUpdateView(UpdateView):
    model = Publicacion
    template_name = 'Blog/publicacion_actualizar.html'
    fields = ['titulo','contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
# ELIMINAR publicacion
class PublicacionDeleteView(DeleteView):
    model = Publicacion
    template_name = 'Blog/publicacion_confirm_delete.html'
    success_url = reverse_lazy('blog-home')


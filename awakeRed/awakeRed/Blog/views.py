from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
from .forms import TweetForm, ContactoForm
from django.contrib import messages
# Create your views here.

def calcular(a,b):
    return a+b
def home(request):
    x = 1
    y = 2
    calcular(x,y)
    contexto ={
        'publicacionesLlave' : Publicacion.objects.raw('SELECT * FROM Blog_publicacion ORDER BY id DESC'),
        'titulo': 'Blog-Landing'
    }
    print(contexto['publicacionesLlave'])
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
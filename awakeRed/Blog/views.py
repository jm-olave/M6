from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

publicaciones = [
    {
        'autor': "Rodrigo",
        'titulo': "Publicacion 1",
        'contenido': "loremp ipsum",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor': "Nicolas",
        'titulo': "Publicacion 2",
        'contenido': "loremp ipsum 2",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor': "Adolfo",
        'titulo': "Publicacion 3",
        'contenido': "loremp ipsum 3",
        'fecha': "13 de julio del 2023"
    }
]
def home(request):
    contexto ={
        'publicacionesLlave': publicaciones
    }
    return render(request,'Blog/index.html', contexto)

def contacto(request):
    return render(request, 'Blog/contacto.html',  {'titulo': "AwakeRed"})
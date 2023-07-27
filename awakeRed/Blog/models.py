from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(default= timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Tweet(models.Model):
    cuerpo = models.TextField(max_length=250)
    fecha = models.DateTimeField(default= timezone.now)

# Comentario
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion,  on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(default= timezone.now)


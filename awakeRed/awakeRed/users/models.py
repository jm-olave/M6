from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='users/img_perfiles')

    def __str__(self):
        return f'este es el perfil del usuario: {self.usuario.username}'
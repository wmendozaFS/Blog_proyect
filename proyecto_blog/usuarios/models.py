from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfiles/', default='default.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

# Create your models here.

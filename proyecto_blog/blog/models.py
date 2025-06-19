from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class Hashtag(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="articulos_likes", blank=True)
    categorias = models.ManyToManyField(Categoria, related_name="articulos", blank=True)
    hashtags = models.ManyToManyField(Hashtag, related_name="articulos", blank=True)
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
            return self.titulo
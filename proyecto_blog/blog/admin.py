from django.contrib import admin
from .models import Categoria, Hashtag, Articulo

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Hashtag)


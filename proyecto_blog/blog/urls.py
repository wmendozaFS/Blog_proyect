from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='blog_home'),
]
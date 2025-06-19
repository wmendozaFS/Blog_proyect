from django.shortcuts import render

def lista_articulos(request):
    return render(request, 'lista_articulos.html')
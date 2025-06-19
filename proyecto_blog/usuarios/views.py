from urllib import request
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def registro(request):
    return render(request, 'registro.html')
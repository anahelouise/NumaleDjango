from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view():
    return HttpResponse("Uma teste string de resposta")

def user_view(request, username):
    return HttpResponse(f"Perfil do Usuario: {username}")

def root_view(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')
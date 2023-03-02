from django.shortcuts import render
from .models import Fotografia

def index(request):      
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
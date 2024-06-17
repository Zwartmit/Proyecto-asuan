from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import *

def vista1(request):
    nombre = {
        'nombre': 'Juan'
    }
    return JsonResponse(nombre)

def vista2(request):
    nombre = {
        'nombre': 'Juan',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'index.html', nombre)
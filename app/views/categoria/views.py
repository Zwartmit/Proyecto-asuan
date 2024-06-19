from typing import Any
from django.views.generic import ListView
from django.shortcuts import render

from app.models import Categoria

def lista_categoria(request):
    
    nombre = {
        
        'titulo': 'Listado de Categorias',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categoria/listar.html',nombre)

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorias'
        return context
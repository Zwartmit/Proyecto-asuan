import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Categoria
from app.forms import CategoriaForm

def lista_categoria(request):
    nombre = {
        'titulo': 'Listado de Categorias',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categoria/listar.html',nombre)

###### LISTAR ######

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorias'
        context['entidad'] = 'Categorías'
        context['listar_url'] = reverse_lazy('app:categoria_crear')
        context['crear_url'] = reverse_lazy('app:categoria_crear')
        return context

###### CREAR ######

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('app:categoria_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear categoria'
        context['clase'] = 'Esta categoría ya existe'
        context['entidad'] = 'Crear categoria'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        return context
    
    def form_valid(self, form):
        categoria = form.cleaned_data.get('categoria').lower()
        
        if Categoria.objects.filter(categoria__iexact=categoria).exists():
            form.add_error('categoria', 'Ya existe una categoría con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('app:categoria_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar categoria'
        context['clase'] = 'Esta categoría ya existe'
        context['entidad'] = 'Categorías'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        return context
    
    def form_valid(self, form):
        categoria = form.cleaned_data.get('categoria').lower()
        
        if Categoria.objects.filter(categoria__iexact=categoria).exists():
            form.add_error('categoria', 'Ya existe una categoría con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### ELIMINAR ######

class CategoriaDeleteView(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('app:categoria_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar categoria'
        context['clase'] = 'Esta categoría ya existe'
        context['entidad'] = 'Categorías'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        return context

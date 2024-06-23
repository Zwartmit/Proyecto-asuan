import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Marca
from app.forms import MarcaForm

def lista_marca(request):
    nombre = {
        'titulo': 'Listado de marcas',
        'marcas': Marca.objects.all()
    }
    return render(request, 'marca/listar.html',nombre)

###### LISTAR ######

class MarcaListView(ListView):
    model = Marca
    template_name = 'marca/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de marcas'
        context['entidad'] = 'Listado de marcas'
        context['listar_url'] = reverse_lazy('app:marca_lista')
        context['crear_url'] = reverse_lazy('app:marca_crear')
        return context

###### CREAR ######

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('app:marca_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar marca'
        context['entidad'] = 'Agregar marca'
        context['error'] = 'Esta marca ya existe'
        context['listar_url'] = reverse_lazy('app:marca_lista')
        return context
    
    def form_valid(self, form):
        marca = form.cleaned_data.get('marca').lower()
        
        if Marca.objects.filter(marca__iexact=marca).exists():
            form.add_error('marca', 'Ya existe una marca con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### EDITAR ######

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('app:marca_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar marca'
        context['entidad'] = 'Editar marca'
        context['error'] = 'Esta marca ya existe'
        context['listar_url'] = reverse_lazy('app:marca_lista')
        return context
    
    def form_valid(self, form):
        marca = form.cleaned_data.get('marca').lower()
        
        if Marca.objects.filter(marca__iexact=marca).exists():
            form.add_error('marca', 'Ya existe una marca con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### ELIMINAR ######

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/eliminar.html'
    success_url = reverse_lazy('app:marca_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar marca'
        context['entidad'] = 'Eliminar marca'
        context['listar_url'] = reverse_lazy('app:marca_lista')
        return context

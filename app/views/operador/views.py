import django
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Operador
from app.forms import OperadorForm

def lista_operador(request):
    nombre = {
        'titulo': 'Listado de operadores',
        'operador': Operador.objects.all()
    }
    return render(request, 'operador/listar.html',nombre)

###### LISTAR ######

class OperadorListView(ListView):
    model = Operador
    template_name = 'operador/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de operadores'
        context['entidad'] = 'Listado de operadores'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        context['crear_url'] = reverse_lazy('app:operador_crear')
        return context

###### CREAR ######

class OperadorCreateView(CreateView):
    model = Operador
    form_class = OperadorForm
    template_name = 'operador/crear.html'
    success_url = reverse_lazy('app:operador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar operador'
        context['entidad'] = 'Agregar operador'
        context['error'] = 'Este operador ya existe'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context
    
###### EDITAR ######

class OperadorUpdateView(UpdateView):
    model = Operador
    form_class = OperadorForm
    template_name = 'operador/crear.html'
    success_url = reverse_lazy('app:operador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar operador'
        context['entidad'] = 'Editar operador'
        context['error'] = 'Esta operador ya existe'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context
    
###### ELIMINAR ######

class OperadorDeleteView(DeleteView):
    model = Operador
    template_name = 'operador/eliminar.html'
    success_url = reverse_lazy('app:operador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar operador'
        context['entidad'] = 'Eliminar operador'
        context['listar_url'] = reverse_lazy('app:operador_lista')
        return context

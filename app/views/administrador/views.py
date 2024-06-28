import django
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Administrador
from app.forms import AdministradorForm

def lista_administrador(request):
    nombre = {
        'titulo': 'Listado de meseros',
        'meseros': Administrador.objects.all()
    }
    return render(request, 'administrador/listar.html',nombre)

###### LISTAR ######

class AdministradorListView(ListView):
    model = Administrador
    template_name = 'administrador/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de administradores'
        context['entidad'] = 'Listado de administradores'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        context['crear_url'] = reverse_lazy('app:administrador_crear')
        return context

###### CREAR ######

class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar administrador'
        context['entidad'] = 'Agregar administrador'
        context['error'] = 'Este administrador ya existe'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        return context
    
###### EDITAR ######

class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('app:administrador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['error'] = 'Esta administrador ya existe'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context
    
###### ELIMINAR ######

class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('app:administrador_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('app:administrador_lista')
        return context

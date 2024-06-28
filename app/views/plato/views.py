import django
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Plato
from app.forms import PlatoForm

def lista_platos(request):
    nombre = {
        'titulo': 'Listado de platos',
        'platos': Plato.objects.all()
    }
    return render(request, 'plato/listar.html',nombre)

###### LISTAR ######

class PlatoListView(ListView):
    model = Plato
    template_name = 'plato/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de platos'
        context['entidad'] = 'Listado de platos'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        context['crear_url'] = reverse_lazy('app:plato_crear')
        return context

###### CREAR ######

class PlatoCreateView(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/crear.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar plato'
        context['entidad'] = 'Agregar plato'
        context['error'] = 'Este plato ya existe'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context
    
    def form_valid(self, form):
        plato = form.cleaned_data.get('plato').lower()
        
        if Plato.objects.filter(plato__iexact=plato).exists():
            form.add_error('plato', 'Ya existe un plato con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

class PlatoUpdateView(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/crear.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar plato'
        context['entidad'] = 'Editar plato'
        context['error'] = 'Este plato ya existe'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context
    
    def form_valid(self, form):
        plato = form.cleaned_data.get('plato').lower()
        
        if Plato.objects.filter(plato__iexact=plato).exists():
            form.add_error('plato', 'Ya existe un plato con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### ELIMINAR ######

class PlatoDeleteView(DeleteView):
    model = Plato
    template_name = 'plato/eliminar.html'
    success_url = reverse_lazy('app:plato_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar plato'
        context['entidad'] = 'Eliminar plato'
        context['listar_url'] = reverse_lazy('app:plato_lista')
        return context

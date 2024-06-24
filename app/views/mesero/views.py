import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Mesero
from app.forms import MeseroForm

def lista_mesero(request):
    nombre = {
        'titulo': 'Listado de meseros',
        'meseros': Mesero.objects.all()
    }
    return render(request, 'mesero/listar.html',nombre)

###### LISTAR ######

class MeseroListView(ListView):
    model = Mesero
    template_name = 'mesero/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de meseros'
        context['entidad'] = 'Listado de meseros'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        context['crear_url'] = reverse_lazy('app:mesero_crear')
        return context

###### CREAR ######

class MeseroCreateView(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/crear.html'
    success_url = reverse_lazy('app:mesero_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar mesero'
        context['entidad'] = 'Agregar mesero'
        context['error'] = 'Este mesero ya existe'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context
    
    def form_valid(self, form):
        mesero = form.cleaned_data.get('mesero').lower()
        
        if Mesero.objects.filter(mesero__iexact=mesero).exists():
            form.add_error('mesero', 'Ya existe un mesero con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### EDITAR ######

class MeseroUpdateView(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/crear.html'
    success_url = reverse_lazy('app:mesero_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar mesero'
        context['entidad'] = 'Editar mesero'
        context['error'] = 'Esta mesero ya existe'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context
    
    def form_valid(self, form):
        mesero = form.cleaned_data.get('mesero').lower()
        
        if Mesero.objects.filter(mesero__iexact=mesero).exists():
            form.add_error('mesero', 'Ya existe un mesero con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### ELIMINAR ######

class MeseroDeleteView(DeleteView):
    model = Mesero
    template_name = 'mesero/eliminar.html'
    success_url = reverse_lazy('app:mesero_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar mesero'
        context['entidad'] = 'Eliminar mesero'
        context['listar_url'] = reverse_lazy('app:mesero_lista')
        return context

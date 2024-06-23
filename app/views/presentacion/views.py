import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Presentacion
from app.forms import PresentacionForm

def lista_presentacion(request):
    nombre = {
        'titulo': 'Listado de presentaciones',
        'presentaciones': Presentacion.objects.all()
    }
    return render(request, 'presentacion/listar.html',nombre)

###### LISTAR ######

class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'presentacion/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de presentaciones'
        context['entidad'] = 'Listado de presentaciones'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        context['crear_url'] = reverse_lazy('app:presentacion_crear')
        return context

###### CREAR ######

class PresentacionCreateView(CreateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/crear.html'
    success_url = reverse_lazy('app:presentacion_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar presentación'
        context['entidad'] = 'Agregar presentación'
        context['error'] = 'Esta presentación ya existe'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context
    
    def form_valid(self, form):
        presentacion = form.cleaned_data.get('presentacion').lower()
        
        if Presentacion.objects.filter(presentacion__iexact=presentacion).exists():
            form.add_error('presentacion', 'Ya existe una presentación con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

class PresentacionUpdateView(UpdateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/crear.html'
    success_url = reverse_lazy('app:presentacion_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar presentación'
        context['entidad'] = 'Editar presentación'
        context['error'] = 'Esta presentación ya existe'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context
    
    def form_valid(self, form):
        presentacion = form.cleaned_data.get('presentacion').lower()
        
        if Presentacion.objects.filter(presentacion__iexact=presentacion).exists():
            form.add_error('presentacion', 'Ya existe una presentación con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### ELIMINAR ######

class PresentacionDeleteView(DeleteView):
    model = Presentacion
    template_name = 'presentacion/eliminar.html'
    success_url = reverse_lazy('app:presentacion_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar presentación'
        context['entidad'] = 'Eliminar presentación'
        context['listar_url'] = reverse_lazy('app:presentacion_lista')
        return context

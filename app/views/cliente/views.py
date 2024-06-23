import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Cliente
from app.forms import ClienteForm

def lista_cliente(request):
    nombre = {
        'titulo': 'Listado de clientes',
        'cliente': Cliente.objects.all()
    }
    return render(request, 'cliente/listar.html',nombre)

###### LISTAR ######

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de clientes'
        context['entidad'] = 'Listado de clientes'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        return context

###### CREAR ######

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar cliente'
        context['entidad'] = 'Agregar cliente'
        context['error'] = 'Este cliente ya está registrado'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context
    
    # def form_valid(self, form):
    #     cliente = form.cleaned_data.get('cliente').lower()
        
    #     if Cliente.objects.filter(cliente__iexact=cliente).exists():
    #         form.add_error('cliente', 'Ya existe un cliente con este nombre.')
    #         return self.form_invalid(form)
    #     return super().form_valid(form)
    
###### EDITAR ######

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar cliente'
        context['entidad'] = 'Editar cliente'
        context['error'] = 'Este cliente ya está registrad'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context
    
    def form_valid(self, form):
        cliente = form.cleaned_data.get('cliente').lower()
        
        if Cliente.objects.filter(cliente__iexact=cliente).exists():
            form.add_error('cliente', 'Ya existe un cliente con este nombre.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
###### ELIMINAR ######

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('app:cliente_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar cliente'
        context['entidad'] = 'Eliminar cliente'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        return context

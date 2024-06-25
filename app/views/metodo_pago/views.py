import django
# from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Metodo_pago
from app.forms import Metodo_pagoForm

def lista_venta(request):
    nombre = {
        'titulo': 'Listado de Metodos de Pago',
        'ventaas': Metodo_pago.objects.all()
    }
    return render(request, 'metodopago/listar.html',nombre)

###### LISTAR ######

class Metodo_pagoListView(ListView):
    model = Metodo_pago
    template_name = 'metodopago/listar.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Metodos de Pago'
        context['entidad'] = 'Listado de Metodos de Pago'
        context['listar_url'] = reverse_lazy('app:metodopago_lista')
        context['crear_url'] = reverse_lazy('app:metodopago_crear')
        return context

###### CREAR ######

class Metodo_pagoCreateView(CreateView):
    model = Metodo_pago
    form_class = Metodo_pagoForm
    template_name = 'metodopago/crear.html'
    success_url = reverse_lazy('app:metodopago_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar medoto de pago'
        context['entidad'] = 'Agregar metodo de pago'
        context['error'] = 'Este metodo de pago ya existe'
        context['listar_url'] = reverse_lazy('app:metodopago_lista')
        return context
    
###### EDITAR ######

class Metodo_pagoView(UpdateView):
    model = Metodo_pago
    form_class = Metodo_pagoForm
    template_name = 'metodopago/crear.html'
    success_url = reverse_lazy('app:metodopago_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Metodo de pago'
        context['entidad'] = 'Editar Metodo de pago'
        context['error'] = 'Este metodo de pago ya existe'
        context['listar_url'] = reverse_lazy('app:metodopago_lista')
        return context
    
###### ELIMINAR ######

class Metodo_pagoDeleteView(DeleteView):
    model = Metodo_pago
    template_name = 'metodopago/eliminar.html'
    success_url = reverse_lazy('app:metodopago_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar metodo de pago'
        context['entidad'] = 'Eliminar metodo de pago'
        context['listar_url'] = reverse_lazy('app:metodopago_lista')
        return context 
    
    
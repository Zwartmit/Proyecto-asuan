import django
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Producto
from app.forms import ProductoForm

def lista_productos(request):
    nombre = {
        'titulo': 'Listado de productos',
        'productos': Producto.objects.all()
    }
    return render(request, 'producto/listar.html',nombre)

###### LISTAR ######

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Juan'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de productos'
        context['entidad'] = 'Listado de productos'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        context['crear_url'] = reverse_lazy('app:producto_crear')
        return context

###### CREAR ######

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar producto'
        context['entidad'] = 'Agregar producto'
        context['error'] = 'Este producto ya existe'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context
    
    def form_valid(self, form):
        producto = form.cleaned_data.get('producto').lower()
        
        if Producto.objects.filter(producto__iexact=producto).exists():
            form.add_error('producto', 'Ya existe un producto con este nombre.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
###### EDITAR ######

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar producto'
        context['entidad'] = 'Editar producto'
        context['error'] = 'Este producto ya existe'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context
    
###### ELIMINAR ######

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/eliminar.html'
    success_url = reverse_lazy('app:producto_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar producto'
        context['entidad'] = 'Eliminar producto'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        return context

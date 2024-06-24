from django.urls import path
from app.views import *
from app.views.categoria.views import *
from app.views.marca.views import *
from app.views.presentacion.views import *
from app.views.producto.views import *
from app.views.cliente.views import *
from app.views.mesero.views import *
from app.views.plato.views import *
from app.views.cuenta.views import *
from app.views.administrador.views import *
from app.views.operador.views import *

app_name = 'app'
urlpatterns = [
    ### CRUD CATEGORÍA ###
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'),

    ### CRUD MARCA ###
    path('marca/listar/', MarcaListView.as_view(), name='marca_lista'),
    path('marca/crear/', MarcaCreateView.as_view(), name='marca_crear'),
    path('marca/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marca_editar'),
    path('marca/eliminar/<int:pk>/', MarcaDeleteView.as_view(), name='marca_eliminar'),

    ### CRUD PRESENTACIÓN ###
    path('presentacion/listar/', PresentacionListView.as_view(), name='presentacion_lista'),
    path('presentacion/crear/', PresentacionCreateView.as_view(), name='presentacion_crear'),
    path('presentacion/editar/<int:pk>/', PresentacionUpdateView.as_view(), name='presentacion_editar'),
    path('presentacion/eliminar/<int:pk>/', PresentacionDeleteView.as_view(), name='presentacion_eliminar'),

    ### CRUD PRODUCTO ###
    path('producto/listar/', ProductoListView.as_view(), name='producto_lista'),
    path('producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),

    ### CRUD CLIENTE ###
    path('cliente/listar/', ClienteListView.as_view(), name='cliente_lista'),
    path('cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
    
    ### CRUD MESERO ###
    path('mesero/listar/', MeseroListView.as_view(), name='mesero_lista'),
    path('mesero/crear/', MeseroCreateView.as_view(), name='mesero_crear'),
    path('mesero/editar/<int:pk>/', MeseroUpdateView.as_view(), name='mesero_editar'),
    path('mesero/eliminar/<int:pk>/', MeseroDeleteView.as_view(), name='mesero_eliminar'),

    ### CRUD PLATO ###
    path('plato/listar/', PlatoListView.as_view(), name='plato_lista'),
    path('plato/crear/', PlatoCreateView.as_view(), name='plato_crear'),
    path('plato/editar/<int:pk>/', PlatoUpdateView.as_view(), name='plato_editar'),
    path('plato/eliminar/<int:pk>/', PlatoDeleteView.as_view(), name='plato_eliminar'),

    ### CRUD CUENTA ###
    path('cuenta/listar/', CuentaListView.as_view(), name='cuenta_lista'),
    path('cuenta/crear/', CuentaCreateView.as_view(), name='cuenta_crear'),
    path('cuenta/editar/<int:pk>/', CuentaUpdateView.as_view(), name='cuenta_editar'),
    path('cuenta/eliminar/<int:pk>/', CuentaDeleteView.as_view(), name='cuenta_eliminar'),

    ### CRUD ADMINISTRADOR ###
    path('administrador/listar/', AdministradorListView.as_view(), name='administrador_lista'),
    path('administrador/crear/', AdministradorCreateView.as_view(), name='administrador_crear'),
    path('administrador/editar/<int:pk>/', AdministradorUpdateView.as_view(), name='administrador_editar'),
    path('administrador/eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),

    ### CRUD OPERADOR ###
    path('operador/listar/', OperadorListView.as_view(), name='operador_lista'),
    path('operador/crear/', OperadorCreateView.as_view(), name='operador_crear'),
    path('operador/editar/<int:pk>/', OperadorUpdateView.as_view(), name='operador_editar'),
    path('operador/eliminar/<int:pk>/', OperadorDeleteView.as_view(), name='operador_eliminar'),
]

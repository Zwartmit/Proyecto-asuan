from django.urls import path
from app.views import *
from app.views.categoria.views import *

app_name = 'app'
urlpatterns = [
    # path('categoria/listar2/', lista_categoria, name= 'categoria_lista2'),
    path('categoria/listar/', CategoriaListView.as_view(), name= 'categoria_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name= 'categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name= 'categoria_editar'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name= 'categoria_eliminar'),
#     path('uno/', vista1),
#     path('dos/', vista2)
]

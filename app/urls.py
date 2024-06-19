from django.urls import path
from app.views.categoria.views import *

app_name = 'app'
urlpatterns = [
    path('categoria/listar/', CategoriaListView.as_view(), name = 'categoria_lista')
#     path('uno/', vista1),
#     path('dos/', vista2)
]

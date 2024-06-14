from django.test import TestCase

# Create your tests here.
# from django.test import TestCase

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from asuan.wsgi import *
from app.models import *

# LISTAR
consulta = Cliente.objects.all()
print(consulta)

# -----------------------------------------
# INSERTAR
# cliente = Cliente(
#     nombre='Carlos',
#     tipo_documento='CC',
#     numero_documento=785632,
#     email='carlos@gmail.com',
#     telefono=84196315
# )
# cliente.save()
# consulta = Cliente.objects.all()
# print(consulta)

# -----------------------------------------

# EDITAR
# c = Tipo.objects.get(id=1)
# print(c.nombre)
# c.nombre='docente'
# c.save()
# print(c.nombre)

# -----------------------------------------

# ELIMINAR
# c = Tipo.objects.get(id=1)
# c.delete()
# consulta = Tipo.objects.all()
# print(consulta)

# -----------------------------------------
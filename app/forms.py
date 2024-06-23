from dataclasses import fields
from django.forms import ModelForm

from django import forms
from django.forms import *
from app.models import *

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].widget.attrs["autofocus"] = True

    class Meta:
        model = Categoria
        fields = "__all__"
        widgets = {
            "categoria": TextInput(
                attrs={
                    "placeholder": "Nombre de la categoria",
                }
            )
        }

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["marca"].widget.attrs["autofocus"] = True

    class Meta:
        model = Marca
        fields = "__all__"
        widgets = {
            "marca": TextInput(
                attrs={
                    "placeholder": "Nombre de la marca",
                }
            )
        }

class PresentacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["presentacion"].widget.attrs["autofocus"] = True

    class Meta:
        model = Presentacion
        fields = "__all__"
        widgets = {
            "presentacion": TextInput(
                attrs={
                    "placeholder": "Nombre de la presentacion",
                }
            )
        }

class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["producto"].widget.attrs["autofocus"] = True

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            "producto": TextInput(
                attrs={
                    "placeholder": "Nombre del producto",
                }
            ),
            "cantidad": NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "Cantidad a registrar",
                }
            ),
            "valor": NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "Valor del producto",
                }
            ),
            "estado": Select(
                choices=[(True, "Activo"), (False, "Inactivo")],
                attrs={
                    "min": 1,
                    "placeholder": "Estado del producto",
                },
            ),
        }

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Nombre del cliente",
                }
            ),
            "tipo_documento": Select(
                attrs={
                    "placeholder": "Tipo de documento",
                }
            ),
            "numero_documento": NumberInput(
                attrs={
                    "min": 8,
                    "placeholder": "Número de documento",
                }
            ),
            "email": EmailInput(
                attrs={
                    "placeholder": "Email",
                }
            ),
            "telefono": NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "Teléfono",
                }
            ),
        }

class MeseroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    class Meta:
        model = Mesero
        fields = "__all__"
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Nombre del mesero",
                }
            ),
            "tipo_documento": Select(
                attrs={
                    "placeholder": "Tipo de documento",
                }
            ),
            "numero_documento": NumberInput(
                attrs={
                    "min": 8,
                    "placeholder": "Número de documento",
                }
            ),
            "email": EmailInput(
                attrs={
                    "placeholder": "Email",
                }
            ),
            "telefono": NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "Teléfono",
                }
            ),
        }

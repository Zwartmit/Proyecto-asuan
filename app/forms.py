from dataclasses import fields
from django.forms import ModelForm

from django.forms import *
from app.models import Categoria

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'categoria': TextInput(
                attrs={
                    'placeholder': ' Ingrese una categoria',
                }
            )
        }
        
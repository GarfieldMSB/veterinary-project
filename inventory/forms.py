from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('prod_nomb', 'precio', 'estado', 'cat_prod','marca_nomb','tip_mascota')
        widgets = {
            'prod_nomb': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'precio': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Corriga, sólo número entero o decimal, ejemplo: 10.50")',
                    'oninput': 'setCustomValidity("")',
                    'placeholder' : '15.50'
                    }),
            'estado': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'cat_prod': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'marca_nomb': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'tip_mascota': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'prod_nomb': _('Nombre del producto'),
            'precio': _('Precio'),
            'estado': _('Estado del producto'),
            'cat_prod': _('Categoría del producto'),
            'marca_nomb': _('Marca del producto'),
            'tip_mascota': _('Tipo de mascota'),
        }
class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('cat_nomb',)
        labels = {
            'cat_nomb': _('Nombre de la categoría'),
        }
        widgets = {
            'cat_nomb': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
        }
class FormMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('marca_nomb',)
        labels = {
            'marca_nomb': _('Nombre de la marca'),
        }
        widgets = {
            'marca_nomb': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
        }
class FormTipomascota(forms.ModelForm):
    class Meta:
        model = Tipomascota
        fields = ('tip_mascota',)
        labels = {
            'tip_mascota': _('Tipo de mascota'),
        }
        widgets = {
            'tip_mascota': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
        }
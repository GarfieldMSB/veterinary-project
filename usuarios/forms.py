from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nomb_usr', 'ap_usr', 'tel_usr', 'cel_usr','dir_usr')
        widgets = {
            'nomb_usr': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'ap_usr': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'tel_usr': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")',
                    'placeholder': '056555555'
                    }),
            'cel_usr': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")',
                    'placeholder': '956555555'
                    }),
            'dir_usr': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'nomb_usr': _('Nombre(s) del usuario'),
            'ap_usr': _('Apellidos de usuario'),
            'tel_usr': _('Teléfono del usuario'),
            'cel_usr': _('Número Celular del usuario'),
            'dir_usr': _('Dirección del usuario'),
        }
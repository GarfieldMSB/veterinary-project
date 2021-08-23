from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class FormMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nomb_mascota', 'tip_mascota', 'genero_mascota', 'raza_mascota',)
        widgets = {
            'nomb_mascota': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'tip_mascota': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'genero_mascota': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'raza_mascota': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'nomb_mascota': _('Nombre de la mascota'),
            'tip_mascota': _('Especie de la mascota'),
            'genero_mascota': _('Elegir Género'),
            'raza_mascota': _('Raza')
        }
class FormMedicina(forms.ModelForm):
    class Meta:
        model = Medicina
        fields = ('nomb_medicina', 'descripcion_med')
        widgets = {
            'nomb_medicina': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'descripcion_med': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'nomb_medicina': _('Nombre de la medicina'),
            'descripcion_med': _('Descripción opcional')
        }
class FormVacuna(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ('nomb_vacuna', 'descripcion_vac')
        widgets = {
            'nomb_vacuna': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    }),
            'descripcion_vac': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'nomb_vacuna': _('Nombre de la vacuna'),
            'descripcion_vac': _('Descripción opcional')
        }

class FormDetalleMascota(forms.ModelForm):
    class Meta:
        model = DetalleMascota
        fields = ('fecha_nacimiento', 'estado', 'adicional')
        widgets = {
            'fecha_nacimiento' : DatePicker(
                    options={
                        'useCurrent': True,
                        'locale': 'es',
                    },
                    attrs={
                        'append': 'fa fa-calendar',
                        'icon_toggle': True
                    }
                ),
            'estado': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'adicional': forms.Textarea(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })}
        labels = {
            'fecha_nacimiento': _('Fecha de Nacimiento'),
            'estado': _('Estado actual'),
            'adicional': _('Comentario Adicional')
        }

class FormRegistroClinico(forms.ModelForm):
    class Meta:
        model = RegistroClinico
        fields = ('motivo', 'fecha_registro', 'prediagnostico', 'indicaciones', 'sistema_afectado')
        widgets = {
            'motivo': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'fecha_registro': DatePicker(
                    options={
                        'useCurrent': True,
                        'collapse': False,
                        'locale': 'es',
                    },
                    attrs={
                        'append': 'fa fa-calendar',
                        'icon_toggle': True
                    }
                ),
            'prediagnostico': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    }),
            'indicaciones': forms.Textarea(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'sistema_afectado': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'motivo': _('Motivo de registro clínico'),
            'fecha_registro': _('Fecha de registro'),
            'prediagnostico': _('Prediagnostico'),
            'indicaciones': _('Indicaciones'),
            'sistema_afectado': _('Sistema afectado'),
        }

class FormDetalleVacuna(forms.ModelForm):
    class Meta:
        model = DetalleVacuna
        fields = ('descripcion_trat_vac',)
        widgets = {
            'descripcion_trat_vac': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'descripcion_trat_vac': _('Descripción')
        }
class FormDetalleMedicina(forms.ModelForm):
    class Meta:
        model = DetalleMedicina
        fields = ('descripcion_trat_med',)
        widgets = {
            'descripcion_trat_med': forms.TextInput(
                attrs={
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'descripcion_trat_med': _('Descripción')
        }

class FormImagenMascota(forms.ModelForm):
    class Meta:
        model = ImagenMascota
        fields = ('mascota_img',)
        
        labels = {
            'mascota_img': _('Seleccionar archivo de imagen')
        }
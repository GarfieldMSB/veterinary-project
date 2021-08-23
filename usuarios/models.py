from django.db import models
from django.core.validators import MinValueValidator 
# las tablas

class Usuario(models.Model):
    nomb_usr = models.CharField(max_length=200)
    ap_usr = models.CharField(max_length=200)
    tel_usr = models.PositiveIntegerField(null=True, blank=True, help_text='Teléfono de contacto', validators=[MinValueValidator(6)])
    cel_usr = models.IntegerField(blank=False, help_text='Celular de contacto', validators=[MinValueValidator(9)])
    dir_usr = models.CharField(max_length=300)
    def __str__(self):
        return self.nomb_usr


    


    
from django.db import models
from usuarios.models import *
from inventory.models import *
import os
from django.utils import timezone

class Mascota(models.Model):
    nomb_mascota = models.CharField(max_length=200)
    tip_mascota = models.ForeignKey(Tipomascota, on_delete=models.CASCADE)
    opciones_genero = (
        ('MACHO', 'Macho'),
        ('HEMBRA', 'Hembra')
    )
    genero_mascota = models.CharField(max_length=10, choices=opciones_genero, default="MACHO")
    raza_mascota = models.CharField(max_length=60, blank=True, null=True)
    propietario_mascota = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomb_mascota

class Medicina(models.Model):
    nomb_medicina = models.CharField(max_length=70)
    descripcion_med = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.nomb_medicina
class Vacuna(models.Model):
    nomb_vacuna = models.CharField(max_length=70)
    descripcion_vac = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nomb_vacuna


class DetalleMascota(models.Model):
    mascota = models.OneToOneField(Mascota, on_delete = models.CASCADE)
    fecha_nacimiento = models.DateField(blank=True, null=True) 
    opciones_estado = (
        ('Activo', 'Activo'),
        ('Complicaciones mínimas', 'Complicaciones mínimas'),
        ('Crítico', 'Crítico'),
        ('Fallecido', 'Fallecido')
    )
    estado = models.CharField(max_length=22, choices=opciones_estado, default='Activo')
    adicional = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.mascota

class RegistroClinico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100, blank=False, null=False)
    fecha_registro = models.DateField(default=timezone.now, blank=False, null=False)
    prediagnostico = models.CharField(max_length=150, blank=True, null=True)
    indicaciones = models.CharField(max_length=250, blank=False, null=False)
    sistema_afectado = models.CharField(max_length=100, blank=True, null=True)

class ImagenMascota(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    mascota_img = models.ImageField(upload_to='images')

class DetalleVacuna(models.Model):
    registro_clinico = models.ForeignKey(RegistroClinico, on_delete=models.CASCADE)
    nomb_vacuna = models.ForeignKey(Vacuna, on_delete = models.CASCADE)
    descripcion_trat_vac = models.CharField(max_length=50)

class DetalleMedicina(models.Model):
    registro_clinico = models.ForeignKey(RegistroClinico, on_delete=models.CASCADE)
    nomb_medicina = models.ForeignKey(Medicina, on_delete = models.CASCADE)
    descripcion_trat_med = models.CharField(max_length=50)


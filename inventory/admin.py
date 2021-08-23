from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categoria, Producto, Marca, Tipomascota)
class ViewAdmin(admin.ModelAdmin):
    pass
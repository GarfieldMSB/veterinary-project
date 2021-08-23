from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Usuario)
class ViewAdmin(admin.ModelAdmin):
    pass
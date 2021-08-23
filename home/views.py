import pytz
import datetime
from django.shortcuts import render
# importamos tablas para generar conteo
from inventory.models import *
from usuarios.models import *
from mascotas.models import *
from todo.models import Task
from django.db.models import Q
from django.utils import timezone

def index(request):
    productos = Producto.objects.count()
    usuarios = Usuario.objects.count()
    mascotas = Mascota.objects.count()
    # tabla y número de items agotados
    items_agotados = Producto.objects.filter(Q(estado='AGOTADO')|Q(estado='BAJO_STOCK')).order_by('estado')
    num_agotados = Producto.objects.filter(estado='AGOTADO').count()
    num_criticos = Producto.objects.filter(estado='BAJO_STOCK').count()
    num_total = num_agotados + num_criticos
    # variables para tareas despues de hoy
    hoy = datetime.datetime.now(tz=pytz.UTC)
    tasks_act = Task.objects.filter(completed=False, due_date__gt=hoy).order_by('due_date')[:5]
    num_tasks_act = tasks_act.count()
    # primeras 3 tareas
    tasks_primeras = Task.objects.filter()[:3]

    context = {
        'header' : 'Inicio',
        'productos': productos,
        'usuarios': usuarios,
        'mascotas': mascotas,
        'items_agotados' : items_agotados,
        'num_agotados' : num_agotados,
        'tasks_act' : tasks_act,
        'num_criticos': num_criticos,
        'num_tasks_act' : num_tasks_act,
        'num_total' : num_total 
    }
    return render(request, 'index.html', context)
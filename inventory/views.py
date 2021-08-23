from django.shortcuts import render, redirect
#añadiendo las tablas
from .models import *
from .forms import *

def index(request):
    items = Producto.objects.all()
    context = {
        'items_prod' : items,
        'header' : 'Inventario de productos'
    }
    return render(request, 'inventario/index.html', context)

def nuevoProd(request):

    if request.method ==  "POST":
        formproducto = FormProducto(request.POST)
        formcat = FormCategoria(request.POST)
        formmarc = FormMarca(request.POST)
        formmasc = FormTipomascota(request.POST)
        if formproducto.is_valid():
            formproducto.save()
            return redirect('inventario:index')
        elif formcat.is_valid():
            formcat.save()
            return redirect('inventario:nuevo_prod')
        elif formmarc.is_valid():
            formmarc.save()
            return redirect('inventario:nuevo_prod')
        elif formmasc.is_valid():
            formmasc.save()
            return redirect('inventario:nuevo_prod')
    else:
        formproducto = FormProducto()
        formcat = FormCategoria()
        formmarc = FormMarca()
        formmasc = FormTipomascota()
        context = {
            'formproducto' : formproducto,
            'formcat' : formcat,
            'formmarc' : formmarc,
            'formmasc' : formmasc,
            'tipo_titulo' : 'Nuevo Producto!',
            'tipo_boton' : 'Guardar Producto',
        }
        return render(request, 'inventario/nuevo_prod.html', context)

def editar_prod(request, item_id):
    item = Producto.objects.get(pk=item_id)
    if request.method == "POST":
        form = FormProducto(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventario:index')
    else:
        form = FormProducto(instance=item)
        context = {
            'form' : form,
            'tipo_titulo' : 'Editar Producto',
            'tipo_boton' : 'Guardar Cambios',
        }
        return render(request, 'inventario/editar_prod.html', context)

def eliminar_prod(request, item_id):
    Producto.objects.filter(pk=item_id).delete()
    items = Producto.objects.all()
    context = {
        'items': items,
    }
    return redirect('inventario:index')


# def nuevoCatMarMasc(request, cls):
#     if request.method ==  "POST":
#         form = cls(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inventario:nuevo_prod')
#     else:
#         form = cls()
#         return render(request, 'inventario/nuevo_prod_1.html', {'form': form})

# def nuevoCat(request):
#     return nuevoCatMarMasc(request, FormCategoria)

# def nuevoMar(request):
#     return nuevoCatMarMasc(request, FormMarca)

# def nuevoMasc(request):
#     return nuevoCatMarMasc(request, FormTipomascota)

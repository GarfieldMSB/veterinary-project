from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

def index(request):
    items = Mascota.objects.all()
    context = {
        'items_mascota' : items,
        'header' : 'Mascotas Registrados',
    }
    return render(request, 'mascotas/index.html', context)
    
# Apartado independiente de crear nueva mascota
# def nueva_mascota(request):
#     if request.method ==  "POST":
#         form = FormMascota(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('mascotas:index')
#     else:
#         form = FormMascota()
#         return render(request, 'mascotas/nueva_mascota.html', {'form': form})

# vista para cada mascota
def perfil_mascota(request, item_id):
    try:
        item_mascota = Mascota.objects.get(pk=item_id)
        item_detalle = DetalleMascota.objects.filter(mascota=item_id)
        item_registro = RegistroClinico.objects.filter(mascota=item_id)
        mascota = get_object_or_404(Mascota, pk=item_id)
        form_det_masc = FormDetalleMascota(request.POST or None)
        form_reg = FormRegistroClinico(request.POST or None)
        item_imagen = ImagenMascota.objects.filter(mascota=item_id)
        form_imagen = FormImagenMascota(request.POST or None, request.FILES or None)

        if form_det_masc.is_valid():
            nform_det_masc = form_det_masc.save(commit=False) # Don't save it yet
            nform_det_masc.mascota = mascota # Add person
            nform_det_masc.save() # Now save it
            return redirect('mascotas:perfil_mascota', item_id=item_id)
        elif form_reg.is_valid():
            nform_reg = form_reg.save(commit=False) # Don't save it yet
            nform_reg.mascota = mascota # Add person
            nform_reg.save() # Now save it
            return redirect('mascotas:perfil_mascota', item_id=item_id)
        elif form_imagen.is_valid():
            nform_imagen = form_imagen.save(commit=False) # Don't save it yet
            nform_imagen.mascota = mascota # Add person
            nform_imagen.save() # Now save it
            return redirect('mascotas:perfil_mascota', item_id=item_id)
        
        
        context = {
        'item_mascota' : item_mascota,
        'item_imagen' : item_imagen,
        'header' : 'Detalles de Mascota: ',
        'item_detalle': item_detalle,
        'item_registro': item_registro,
        'form_det_masc': form_det_masc,
        'form_reg' : form_reg,
        'form_imagen' : form_imagen
        }
    except Mascota.DoesNotExist:
        raise Http404("Mascota no existe")
    return render(request, 'mascotas/perfil.html', context)

def editar_detalle(request, item_id):
    item = DetalleMascota.objects.get(pk=item_id)
    
    if request.method == "POST":
        form = FormDetalleMascota(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mascotas:perfil_mascota', item_id=item_id)
    else:
        form = FormDetalleMascota(instance=item)
        context = {
            'tipo_form': 'detalle', 
            'form' : form,
            'item': item
        }
        return render(request, 'mascotas/editar_detalle.html', context)
    
def editar_registro(request, item_id):
    item = RegistroClinico.objects.get(pk=item_id)
    mascota = Mascota.objects.get(pk=item.mascota.id)
    if request.method == "POST":
        form = FormRegistroClinico(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mascotas:perfil_mascota', item_id=mascota.pk)
    else:
        form = FormRegistroClinico(instance=item)
        context = {
            'tipo_form': 'registro',
            'form' : form,
            'item': item,
        }
        return render(request, 'mascotas/editar_detalle.html', context)


def eliminar_imagen(request, item_id):
    item = ImagenMascota.objects.get(pk=item_id)
    mascota = Mascota.objects.get(pk=item.mascota.id)
    item.delete()
    return redirect('mascotas:perfil_mascota', item_id=mascota.pk)



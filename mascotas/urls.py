from django.urls import path
from . import views

app_name = 'mascotas'
urlpatterns = [
    path('', views.index, name='index'),
    # path('nueva_mascota/', views.nueva_mascota, name='nueva_mascota'),
    path('<int:item_id>/', views.perfil_mascota, name='perfil_mascota'),
    path('<int:item_id>/editar_detalle', views.editar_detalle, name='editar_detalle'),
    path('editar_registro/<int:item_id>', views.editar_registro, name='editar_registro'),
    path('<int:item_id>/eliminar_imagen/', views.eliminar_imagen, name='eliminar_imagen'),
]
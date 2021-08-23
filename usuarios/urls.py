from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_usuario/', views.nuevo_usr, name='nuevo_usr'),
    path('<int:item_id>/', views.perfil_usr, name='perfil_usr'),
    path('<int:item_id>/editar', views.editar_usr, name='editar_usr'),
    path('<int:item_id>/eliminar', views.eliminar_usr, name='eliminar_usr'),
    # path('<int:item_id>/Nueva_mascota', views.nueva_mascota_perfil_usr, name='nueva_mascota_perfil_usr'),
]
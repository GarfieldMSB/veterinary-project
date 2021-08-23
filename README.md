Proyecto universitario de un Sistema Web Gestor de Veterinaria

#### Construido con:
- Python
- Django 
- SBAdmin2 Template 

#### Funcionalidades:
* Gestión de Inventario
* Gestión de Usuarios
* Gestión de Mascotas por Usuario
* Perfil e Historial Clínico de Mascotas
* Agenda - Lista de Tareas


#### Cómo construirlo:
```
#Instalar los requerimientos
pip install -r requirements.txt 

#migrar la base de datos
py manage.py migrate 

#Crea el administrador de Django
py manage.py createsuperuser

#Correr el server localmente
py manage.py runserver 


```

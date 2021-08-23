from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventory.urls')),
    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('agenda/', include('todo.urls', namespace="todo")),
    # path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

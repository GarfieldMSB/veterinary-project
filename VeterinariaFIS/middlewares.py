from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from . import settings

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware que hace requerido la autentificacion del usuario para poder
    visualizar cualquier otra pagina que no se le haya sido especificada
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), """
        El middleware Login Rquired debe estar luego de AuthenticationMiddleware.
        es necesario incluir el template context_processor:
        'django.contrib.auth.context_processors.auth'."""

        if not request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(settings.AUTH_LOGIN_ROUTE))
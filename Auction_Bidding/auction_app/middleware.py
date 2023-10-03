
from django.http import HttpResponseForbidden

class AdminAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        static_api_secret = request.META.get('HTTP_STATIC_API_SECRET')

        if static_api_secret == 'your_static_secret_key':
            request.is_admin = True
        else:
            request.is_admin = False

        response = self.get_response(request)
        return response

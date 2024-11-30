from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(reverse('login')) and not request.path.startswith(reverse('register')):
            return redirect('login')  # Redirige a la página de inicio de sesión
        return self.get_response(request)

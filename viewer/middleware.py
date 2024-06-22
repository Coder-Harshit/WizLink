from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not any(request.path.startswith(url) for url in settings.LOGIN_EXEMPT_URLS):
                return redirect(settings.LOGIN_URL + '?next=' + request.path)
        return self.get_response(request)
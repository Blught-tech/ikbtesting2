from django.shortcuts import redirect
from django.urls import reverse

from .models import UserMFA


class MfaRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            mfa_profile = UserMFA.objects.filter(user=request.user, is_enabled=True).only('id').first()
            if mfa_profile and not request.session.get('mfa_verified'):
                mfa_verify_url = reverse('mfa_verify')
                logout_url = reverse('logout')
                admin_logout_url = reverse('admin_logout')
                if request.path not in {mfa_verify_url, logout_url, admin_logout_url}:
                    return redirect(f"{mfa_verify_url}?next={request.path}")
        return self.get_response(request)

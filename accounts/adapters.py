# accounts/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.urls import reverse

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        # запрет автосоздания
        return False

    def get_signup_redirect_url(self, request, sociallogin):
        # жёсткий редирект на твой кастомный register
        return reverse("register")
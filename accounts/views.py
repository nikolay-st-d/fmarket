from django.contrib.auth.views import LoginView
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

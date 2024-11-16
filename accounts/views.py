from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import AccountUserCreationForm


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class RegisterUserView(CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


class LogoutUserView(LogoutView):
    template_name = 'accounts/logout.html'

from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, DeleteView
from accounts.forms import AccountUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutUserView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'accounts/logout.html'


class UserPasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/password-change.html'

    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully!")
        return super().form_valid(form)


class RegisterUserView(CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        message = "Profile created! Please complete all fields to access all site features."
        messages.success(self.request, message)
        return response

    def get_success_url(self):
        return reverse('edit-user', kwargs={'pk': self.object.pk})


class DeleteUserView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/delete-user.html'
    model = UserModel
    success_url = reverse_lazy('index')


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = 'first_name', 'last_name', 'country', 'phone_number'
    template_name = 'accounts/edit-user.html'

    def get_success_url(self):
        return reverse('edit-user', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.phone_number = form.cleaned_data['phone_number'].replace(' ', '')
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)


class UserPasswordResetView(LoginRequiredMixin, auth_views.PasswordResetView):
    template_name = 'accounts/password-reset.html'


# TODO: Have to check the following 3 classes in production.
# TODO: These will need SMTP server to work
class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/account.html'
    success_url = reverse_lazy('password_reset_done')


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password-reset-confirm.html'


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/account.html'


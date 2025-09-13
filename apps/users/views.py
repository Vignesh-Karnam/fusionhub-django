from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm

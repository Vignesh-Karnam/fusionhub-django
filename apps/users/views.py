from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from .forms import CustomAuthenticationForm, CustomPasswordResetForm
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    pass

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
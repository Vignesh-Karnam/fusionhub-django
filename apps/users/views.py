from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .forms import CustomAuthenticationForm, CustomPasswordResetForm, CustomSetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email_html.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy("users:password_reset_complete")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'

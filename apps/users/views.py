from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView
)
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import (
    CustomAuthenticationForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    CustomUserCreationForm
)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if remember_me:
            self.request.session.set_expiry(1209600)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    pass


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

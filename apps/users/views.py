from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "input-field", "placeholder": "Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input-field", "placeholder": "Password"})
    )

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "input-field", "placeholder": "Email"}),
        }


from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-field"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-field"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-field"}))


from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input-field"}))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-field"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-field"}))

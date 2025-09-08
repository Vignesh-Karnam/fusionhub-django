from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5', 
                'placeholder': 'name@company.com' 
            }
        ),
        required=True
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': '••••••••'
            }
        ),
        required= True
    )
    remember_me = forms.CharField(
        label=_('Remember me'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300'
            }
        ),
        required=True
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

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
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
    password1 = forms.CharField(
        label=_('Password'),
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': '••••••••'
            }
        ),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': '••••••••'
            }
        ),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )


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


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': 'name@company.com'
            }
        ),
        required=True
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_('New password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': '••••••••'
            }
        ),
        strip=False,
        required=True
    )
    new_password2 = forms.CharField(
        label=_('New password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
                'placeholder': '••••••••'
            }
        ),
        strip=False,
        required=True
    )

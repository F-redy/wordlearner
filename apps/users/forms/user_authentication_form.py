from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


class AuthenticationUserForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter your email'),
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Enter your password'),
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

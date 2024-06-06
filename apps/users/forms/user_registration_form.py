from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.users.utils import validate_password_length

User = get_user_model()


class RegistrationUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }
        ),
    )
    username = forms.CharField(
        label=_('Username'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username'),
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password'),
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password confirmation'),
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(_('Ця електронна адреса вже зареєстрована!'))
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password_length(password1)
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        validate_password_length(password2)
        return password2

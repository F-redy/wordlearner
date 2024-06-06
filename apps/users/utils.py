from django import forms
from django.utils.translation import gettext_lazy as _


def validate_password_length(password: str):
    min_length = 8
    max_length = 128

    if len(password) < min_length:
        raise forms.ValidationError(
            _('Password must contain at least %(min_length)d characters.') % {'min_length': min_length})
    if len(password) > max_length:
        raise forms.ValidationError(
            _('The password must contain no more than %(max_length)d characters.') % {'max_length': max_length})
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from apps.users.forms import RegistrationUserForm


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': _('Registration')}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

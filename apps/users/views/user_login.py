from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from apps.users.forms import AuthenticationUserForm


class LoginUserView(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'users/login.html'
    extra_context = {'title': _('Login')}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

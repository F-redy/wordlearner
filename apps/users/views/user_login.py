from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
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

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.get_user()
        # if user.is_email_verified is False:
            # send_email_for_verify.apply_async(args=(user.id, self.request.build_absolute_uri(None)))
            # messages.error(self.request, _('Щоб завершити реєстрацію, перевірте свій email.'))
            # logout(self.request)
            # return redirect('users:login')
        # messages.success(self.request, _('Авторизація успішна! Ласкаво просимо на сайт.'))
        return response

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse('/'))

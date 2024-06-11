from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
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

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            user = authenticate(email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password1'))
            # if user.is_active is False or user.is_email_verified is False:
            #     # send_email_for_verify.apply_async(args=(user.id, self.request.build_absolute_uri('/')))
            #     # messages.success(self.request, _('Щоб завершити реєстрацію, перевірте свій email.'))
            return response
        except IntegrityError:
            # messages.error(self.request, _('Користувач із такою адресою електронної пошти вже існує.'))
            return redirect('/')

    def get_success_url(self):
        return reverse_lazy('/')

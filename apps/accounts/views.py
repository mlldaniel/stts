from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.accounts.forms import RegisterForm
from apps.accounts.mixins import LoggedOutOnlyView


class RegisterView(LoggedOutOnlyView, FormView):
    form_class = RegisterForm
    template_name = 'accounts/accounts_register.html'
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

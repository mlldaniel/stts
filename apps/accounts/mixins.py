from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("speech_results:list")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("accounts:login")

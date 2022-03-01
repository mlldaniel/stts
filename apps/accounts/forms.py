from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.accounts.models import Account


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            Account.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except Account.DoesNotExist:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Password confirmation does not match!")
        else:
            return password1

    def save(self, *args, **kwargs):
        user: Account = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        user.username = email
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.username = email
        user.set_password(password)
        user.save()


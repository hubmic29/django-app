from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-xl border px-3 py-2 focus:outline-none focus:ring",
            "placeholder": "np. jan_kowalski",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-xl border px-3 py-2 focus:outline-none focus:ring",
            "placeholder": "np. janek@mail.com",
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-xl border px-3 py-2 focus:outline-none focus:ring",
            "placeholder": "Wpisz hasło",
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-xl border px-3 py-2 focus:outline-none focus:ring",
            "placeholder": "Powtórz hasło",
        })
    )
    class Meta:
        model = User
        fields = ["username", "email"]

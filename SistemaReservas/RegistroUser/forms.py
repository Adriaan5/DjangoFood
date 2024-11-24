from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LoginUsuario

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=15, required=False)

    class Meta:
        model = LoginUsuario
        fields = ['username', 'email', 'telefono', 'password1', 'password2']

class VerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, required=True)

class CustomLoginForm(forms.Form):
    identifier = forms.CharField(label="Correo o teléfono", required=True)
    password = forms.CharField(widget=forms.PasswordInput)

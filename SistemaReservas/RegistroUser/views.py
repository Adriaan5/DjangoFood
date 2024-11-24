from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mass_mail
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, CustomLoginForm, VerificationForm
from .models import LoginUsuario

import random

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_code(user)
            messages.success(request, 'Te hemos enviado un código de verificación.')
            return redirect('verify')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})

def send_verification_code(user):
    code = random.randint(100000, 999999)
    user.verificacion_code = str(code)  
    user.save()

    if user.telefono:
        print(f"Código enviado a {user.telefono}: {code}")
    else:
        send_mass_mail(
            'Código de verificación',
            f'Tu código de verificación es {code}',
            'apereyras@autonoma.edu.pe',
            [user.email],
            fail_silently=False,
        )

def verify_view(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['verification_code']
            try:
                user = LoginUsuario.objects.get(verificacion_code=code)
                user.esta_verificado = True  
                user.verificacion_code = None
                user.save()
                messages.success(request, '¡Cuenta verificada con éxito!')
                return redirect('login')
            except LoginUsuario.DoesNotExist:
                messages.error(request, 'Código incorrecto.')
    else:
        form = VerificationForm()
    return render(request, 'register/verify.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get('identifier')
            password = form.cleaned_data.get('password')

            user = None
            if '@' in identifier:
                try:
                    user = LoginUsuario.objects.get(email=identifier)
                except LoginUsuario.DoesNotExist:
                    messages.error(request, 'Usuario no encontrado.')
                    return render(request, 'register/login.html', {'form': form})
            else:
                try:
                    user = LoginUsuario.objects.get(telefono=identifier)
                except LoginUsuario.DoesNotExist:
                    messages.error(request, 'Usuario no encontrado.')
                    return render(request, 'register/login.html', {'form': form})

            if user and user.esta_verificado:
                authenticated_user = authenticate(request, username=user.username, password=password)

                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect('comidas')
                else:
                    messages.error(request, 'Contraseña incorrecta.')
            else:
                messages.error(request, 'Usuario no encontrado o no verificado.')
    else:
        form = CustomLoginForm()

    return render(request, 'register/login.html', {'form': form})



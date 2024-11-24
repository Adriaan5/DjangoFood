from django.contrib import admin
from .models import LoginUsuario

class LoginUsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telefono', 'esta_verificado')  
    search_fields = ('username', 'email', 'telefono') 

admin.site.register(LoginUsuario, LoginUsuarioAdmin)

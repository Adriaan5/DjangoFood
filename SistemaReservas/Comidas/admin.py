from django.contrib import admin
from .models import SeleccionTipoComida
# Register your models here.

class SeleccionTipoComidAdmin(admin.ModelAdmin):
    list_display = ('nombre_comida', 'usuario')

admin.site.register(SeleccionTipoComida, SeleccionTipoComidAdmin)

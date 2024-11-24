from django.contrib import admin
from .models import Restaurantes, Reserva
# Register your models here.

class RestaurantesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'tipo_comida')
    search_fields = ('nombre', 'direccion')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_hora', 'num_personas', 'id_reserva')
    search_fields = ('usuario', 'fecha_hora', 'num_personas', 'id_reserva')

admin.site.register(Restaurantes, RestaurantesAdmin)
admin.site.register(Reserva, ReservaAdmin)

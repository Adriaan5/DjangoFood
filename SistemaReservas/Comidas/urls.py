from django.urls import path
from . import views

urlpatterns = [
    path('comidas/', views.comidas, name='comidas'),
    path('buscar_restaurantes/', views.buscar_restaurantes, name='buscar_restaurantes')
]
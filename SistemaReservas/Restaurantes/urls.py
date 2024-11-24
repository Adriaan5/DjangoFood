from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),  
    path('logout/', views.logout_view, name='logout'),  
    path('reserva/', views.solicitar_reserva, name='solicitar_reserva'),
    path('reserva_exitosa/<str:id_reserva>/', views.reserva_exitosa, name='reserva_exitosa'),
    path('cancelar/', views.cancelar_reserva, name='cancelar_reserva'),
    path('modificar/', views.modificar_reserva, name='modificar_reserva'),
    path('modificacion/<str:id_reserva>', views.modificacion, name='modificacion'),
]

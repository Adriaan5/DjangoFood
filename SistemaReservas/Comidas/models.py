from django.db import models
from RegistroUser.models import LoginUsuario

# Create your models here. 

class SeleccionTipoComida(models.Model):
    nombre_comida = models.CharField(max_length=20)
    usuario = models.ForeignKey(LoginUsuario, on_delete=models.CASCADE)
  
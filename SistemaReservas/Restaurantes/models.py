from django.db import models
import string, random
from RegistroUser.models import LoginUsuario
from Comidas.models import SeleccionTipoComida


# Create your models her

class Restaurantes(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    tipo_comida = models.ForeignKey(SeleccionTipoComida,on_delete= models.CASCADE)
    descripcion = models.TextField()
    latitud = models.FloatField() 
    longitud = models.FloatField()
    
def GenerarID():
    return "".join(random.choices(string.digits, k=8))

class Reserva(models.Model):
    usuario = models.ForeignKey(LoginUsuario, on_delete=models.CASCADE)
    fecha_hora =models.DateTimeField()
    num_personas = models.IntegerField()
    id_reserva =models.CharField(max_length=10, default=GenerarID, unique=True, primary_key=True, editable=False)
    


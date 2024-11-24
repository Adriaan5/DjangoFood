from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class LoginUsuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10, unique=True, null=False, blank=True)
    esta_verificado = models.BooleanField(default=False)
    verificacion_code = models.CharField(max_length=6, blank=True, null=True)

    ### En un futuro si related_name da errores cambiar el parametro 

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='loginusuario_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='loginusuario_permissions',  
        blank=True
    )


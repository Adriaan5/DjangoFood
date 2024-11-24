# Generated by Django 5.1.3 on 2024-11-24 01:02

import Restaurantes.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Comidas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('fecha_hora', models.DateTimeField()),
                ('num_personas', models.IntegerField()),
                ('id_reserva', models.CharField(default=Restaurantes.models.GenerarID, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('tipo_comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comidas.selecciontipocomida')),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-22 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Videojuego', '0011_remove_usuarios_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='reto',
            name='finalizado',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reto',
            name='tiempoMenor',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reto',
            name='tiempoTotal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='ultimo_inicio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reto',
            name='nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Videojuego.usuarios'),
        ),
    ]

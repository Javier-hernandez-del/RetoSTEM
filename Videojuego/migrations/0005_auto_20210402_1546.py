# Generated by Django 3.1.7 on 2021-04-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videojuego', '0004_auto_20210401_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
                ('minutos_jugados', models.FloatField()),
                ('ultimo_inicio', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='MinutosJugados',
        ),
    ]

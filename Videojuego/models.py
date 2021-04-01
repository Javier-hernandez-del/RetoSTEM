from django.db import models

# Create your models here.

class MinutosJugados(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

class Edades(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    minutos_jugados = models.FloatField()
    ultimo_inicio= models.DateField()

class Edades(models.Model):
    nombre = models.ForeignKey(Usuarios, on_delete=models.SET_NULL,null=True,blank=True)
    edad = models.IntegerField()

class PermanenciaEnLinea(models.Model):
    nombre = models.CharField(max_length=30)
    permanencia = models.IntegerField()

class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()
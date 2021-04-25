from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    area_fav = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    #last_login = models.DateTimeField(auto_now=True)


class MinijuegoCompu(models.Model):
    nombre = models.ForeignKey(Usuarios,on_delete=models.SET_NULL,null=True,blank=True)
    tiempo_jugado_compu = models.FloatField()
    nivel_actual_compu = models.IntegerField()
    scoreCompu = models.IntegerField()
    intentos_por_nivel_compu = models.IntegerField()

class MinijuegoFisica(models.Model):
    nombre = models.ForeignKey(Usuarios,on_delete=models.SET_NULL,null=True,blank=True)
    tiempo_jugado_fisica = models.FloatField()
    nivel_actual_fisica = models.IntegerField()
    scoreFisica = models.IntegerField()
    intentos_por_nivel_fisica = models.IntegerField()

class MinijuegoQuimica(models.Model):
    nombre = models.ForeignKey(Usuarios,on_delete=models.SET_NULL,null=True,blank=True)
    #nombreQ = models.CharField(max_length=30)
    tiempo_jugado_quimica = models.IntegerField()
    nivel_actual_quimica = models.IntegerField()
    scoreQuimica = models.IntegerField()
    intentos_por_nivel_quimica = models.IntegerField()

from django.shortcuts import render
from django.http import HttpResponse
from . models import Reto

# Create your views here.

def index(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')
    return render(request,'index.html')

def GAMESTEAM(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')
    return render(request,'GAMESTEAM.html')

def Estadisticas(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')
    return render(request,'Estadisticas.html')

def proceso(request):
    nombre = request.POST['Nombre']
    nombre = nombre.upper()
    return render(request,'GAMESTEAM.html',{'Name':nombre})

def datos(request):
    jugadores = Reto.objects.all() #select * from Reto;
    return render(request, 'datos.html',{'lista_jugadores':jugadores})
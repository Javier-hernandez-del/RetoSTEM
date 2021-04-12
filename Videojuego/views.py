from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Usuarios
from . models import Edades

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
    jugadores = Usuarios.objects.all() #select * from Reto;
    return render(request, 'datos.html',{'lista_jugadores':jugadores})

#def datos2(request):
 #   jugadores2 = Edades.objects.all() #select * from Reto;
  #  return render(request, 'datos.html',{'lista2_jugadores':jugadores2})

@csrf_exempt
def unity(request):
      retorno = {"nombreUsuario":"Juan", "score":"5500"}
      return JsonResponse(retorno)l
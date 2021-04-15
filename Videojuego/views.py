from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from json import loads
from . models import Usuarios
from . models import Edades
import psycopg2

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

def EstadisticasGlobales(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')
    return render(request,'EstadisticasGlobales.html')

def proceso(request):
    nombre = request.POST['Nombre']
    nombre = nombre.upper()
    return render(request,'GAMESTEAM.html',{'Name':nombre})

def register(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GAMESTEAM')
            #return redirect('Estadisticas')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def datos(request):
    jugadores = Usuarios.objects.all() #select * from Reto;
    return render(request, 'datos.html',{'lista_jugadores':jugadores})

@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    edad = resultados[0].edad
    genero = resultados[0].genero
    ultimo_inicio = resultados[0].ultimo_inicio
    if genero == "Masculino":
        carreras = "QFB, Actuaría, Matemáticas Puras"
    else:
        carreras = "Ingeniería en Software, Mecatrónica"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"score":score, "edad":edad, "genero":genero, "ultimo_inicio":ultimo_inicio, "carreras":carreras})

"""@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    edad = resultados[0].edad
    genero = resultados[0].genero
    ultimo_inicio = resultados[0].ultimo_inicio
    if genero == "Masculino":
        carreras = "QFB, Actuaría, Matemáticas Puras"
    else:
        carreras = "Ingeniería en Software, Mecatrónica"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"score":score, "edad":edad, "genero":genero, "ultimo_inicio":ultimo_inicio, "carreras":carreras})
"""

"""@login_required
def Jugar(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    edad = resultados[0].edad
    genero = resultados[0].genero
    ultimo_inicio = resultados[0].ultimo_inicio
    if genero == "Masculino":
        carreras = "QFB, Actuaría, Matemáticas Puras"
    else:
        carreras = "Ingeniería en Software, Mecatrónica"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"score":score, "edad":edad, "genero":genero, "ultimo_inicio":ultimo_inicio, "carreras":carreras})
"""

"""@login_required
def edad(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    edad = resultados[0].edad
    return render(request, 'score.html', {"nombreUsuario":nombre,"edad":edad})
"""



@csrf_exempt
def unity(request):
      nombre = "Martin"
      score = "1234"
      retorno = {"nombreUsuario":nombre, "score":score}
      return JsonResponse(retorno)


@csrf_exempt
def buscaJugadorBody(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)


@csrf_exempt
def ejemploSQL(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    nombre = ""
    score = ""
    #Create a connection credentials to the PostgreSQL database
    try:
        connection = psycopg2.connect(
            user = "diegomanzanarez",
            password = "STEAMDBpsw07",
            host = "localhost",
            port = "5432",
            database = "steamdb"
        )

        #Create a cursor connection object to a PostgreSQL instance and print the connection properties.
        cursor = connection.cursor()
        #Display the PostgreSQL version installed
        cursor.execute("SELECT * from Videojuego_usuarios;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == jugador_nombre:
                nombre = row[1]
                score = row[2]
            print (row)

    #Handle the error throws by the command that is useful when using python while working with PostgreSQL
    except(Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)
        connection = None

    #Close the database connection
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

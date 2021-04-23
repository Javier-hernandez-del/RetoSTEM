from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from json import loads, dumps
from . models import Usuarios
from . models import Edades
from . models import PermanenciaEnLinea
from . models import MinijuegoCompu, MinijuegoFisica, MinijuegoQuimica
from random import randrange
import psycopg2
import datetime

# Create your views here.

def grafica(request):
    return render(request,'grafica.html')

def index(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')

    return render(request,'index.html')

def grafica(request):
    #data = [['Age', 'Weight'],[ 8,      12],[ 4,      5.5],[ 11,     14],[ 4,      5],[ 3,      3.5],[ 6.5,    7]]
    data = [['Edad', 'Peso']]
    for i in range(0,11):
        x = randrange(100)
        y = randrange(100)
        data.append([x,y])
    datos_formato = dumps(data)
    return render(request,'grafica.html', {'losDatos':datos_formato})

def barras(request):
    '''
    data = [
          ['Year', 'Sales', 'Expenses', 'Profit'],
          ['2014', 1000, 400, 200],
          ['2015', 1170, 460, 250],
          ['2016', 660, 1120, 300],
          ['2017', 1030, 540, 350]
        ]
    '''
    data = [['Nombre', 'Minutos jugados']]
    resultados = PermanenciaEnLinea.objects.all() #select * from Reto;
    for i in resultados:
        x = i.nombre
        y = i.permanencia
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Minutos jugados totales'
    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'barras.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})

def nuevo_usuario(request):
    nombre = request.POST['Nombre']
    edad = request.POST['Edad']
    genero = request.POST['Genero']
    correo = request.POST['Correo']
    contrasena = request.POST['Contrasena']
    area_fav = request.POST['Area']
    #ultimo_inicio = datetime.datetime.now().date()
    #last = User.objects.get(username=nombre).last_login
    u1 = Usuarios(nombre=nombre, edad=edad, genero=genero, area_fav=area_fav)
    u = User.objects.create_user(username=nombre, email=correo, password=contrasena)
    u1.save()
    u.save()
    #return render(request, 'registration/login.html')
    return render(request, 'GAMESTEAM.html')

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


"""
@csrf_exempt
def verificar_usuario(request):
    nombre = "Diego"
    retorno = {"nombreUsuario":nombre}
    return JsonResponse(retorno)
"""

@csrf_exempt
def verificar_usuario(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    retorno = {"nombreUsuario":nombre}
    return JsonResponse(retorno)

"""
@csrf_exempt
def score(request):
    nombre = "Diego"
    score = "1234"
    retorno = {"nombreUsuario":nombre,"Score":score}
    return JsonResponse(retorno)
"""

@csrf_exempt
def score(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    score = "10"
    retorno = {"nombreUsuario":nombre, "puntuacion":score}
    return JsonResponse(retorno)


"""
@csrf_exempt
def guardar_nivel(request):
    nombre = "Diego"
    nivel = "2"
    retorno = {"nombreUsuario":nombre,"nivelQuimica":nivel}
    return JsonResponse(retorno)
"""

@csrf_exempt
def guardar_nivel(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    nivel = "2"
    retorno = {"nombreUsuario":nombre, "nivel":nivel}
    return JsonResponse(retorno)

"""
@csrf_exempt
def guardar_login(request):
    nombre = "Diego"
    login = "2021-04-08"
    retorno = {"nombreUsuario":nombre,"Login":login}
    return JsonResponse(retorno)
"""

@csrf_exempt
def guardar_login(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    last_login = "2021-04-19"
    retorno = {"nombreUsuario":nombre, "ultimo_inicio":last_login}
    return JsonResponse(retorno)

"""

@csrf_exempt
def genero(request):
    nombre = "Diego"
    genero = "Masculino"
    retorno = {"nombreUsuario":nombre,"Genero":genero}
    return JsonResponse(retorno)
"""

@csrf_exempt
def get_genero(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Usuarios.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    genero = resultados[0].genero
    retorno = {"nombreUsuario":nombre, "genero":genero}
    return JsonResponse(retorno)


@csrf_exempt
def buscaJugadorBody(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Reto.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

"""
def barras(request):
    '''
    data = [
          ['Year', 'Sales', 'Expenses', 'Profit'],
          ['2014', 1000, 400, 200],
          ['2015', 1170, 460, 250],
          ['2016', 660, 1120, 300],
          ['2017', 1030, 540, 350]
        ]
    '''
    data = [['Nombre', 'Minutos jugados']]
    resultados = PermanenciaEnLinea.objects.all() #select * from Reto;
    for i in resultados:
        x = i.nombre
        y = i.permanencia
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Minutos jugados totales'
    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'barras.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato}"""
    

@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    edad = resultados[0].edad
    genero = resultados[0].genero
    xuser = Usuarios.objects.get(nombre=usuario)
    last_login = xuser.last_login
    if genero == "Masculino":
        carreras = "QFB, Actuaría, Matemáticas Puras"
    else:
        carreras = "Ingeniería en Software, Mecatrónica"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"edad":edad, "genero":genero, "carreras":carreras, "last_login_":last_login})
 
"""@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Reto.objects.filter(nombre=usuario)
    nombre = resultados[0].Username
    #if genero == "Masculino":
     #   carreras = "QFB, Actuaría, Matemáticas Puras"
    #else:
    #    carreras = "Ingeniería en Software, Mecatrónica"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre})"""




@csrf_exempt
def unity(request):
      nombre = "Martin"
      score = "1234"
      retorno = {"nombreUsuario":nombre, "score":score}
      return JsonResponse(retorno)

"""
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
    """


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

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from json import loads, dumps
from . models import Usuarios
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

def nuevo_usuario(request):
    resultados = Usuarios.objects.all()
    nombre = request.POST['Nombre']
    edad = request.POST['Edad']
    genero = request.POST['Genero']
    correo = request.POST['Correo']
    contrasena = request.POST['Contrasena']
    area_fav = request.POST['Area']
    for i in resultados:
        if(nombre == i.nombre):
            return (render(request, 'nomatch.html'))
    #ultimo_inicio = datetime.datetime.now().date()
    #last = User.objects.get(username=nombre).last_login
    u1 = Usuarios(nombre=nombre, edad=edad, genero=genero, area_fav=area_fav,  password=contrasena)
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

def nomatch(request):
    #return HttpResponse('<h1> Saludos desde Django</h1>')
    return render(request,'nomatch.html')

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


@csrf_exempt
def login_unity(request):
    resultados = Usuarios.objects.all()

    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    jugador_nombre = body['nombre']
    print(jugador_nombre)
    jugador_password = body['password']
    print(jugador_password)
    #x= User.objects.filter(username = jugador_nombre)
    for s in resultados:
        if(s.nombre == jugador_nombre):
            n = Usuarios.objects.filter(nombre=jugador_nombre)
            t=True
        else:
            t=False
    if(t):
        print(n)
        contra = n[0].password
        print(contra)
        if(contra==jugador_password):
            retorno = {"Success":True}
            return JsonResponse(retorno)
        else:
            retorno = {}
            return JsonResponse(retorno)
    else:
        retorno = {}
        return JsonResponse(retorno)


@csrf_exempt
def buscaJugadorBodyQuimca(request):
    print("Este es el body: ")
    print(request.body)
    print("antes del decode")
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    print("Antes del load")
    body_json = loads(body_unicode)
    print("despues del decode")
    jugador_nombre = body_json['nombre']
    intentos_por_nivel_quimica = body_json['intentos_por_nivel_quimica']
    tiempo_jugado_quimica = body_json['tiempo_jugado_quimica']
    nivel_actual_quimica = body_json['nivel_actual_quimica']
    scoreQuimica = body_json['scoreQuimica']
    print (jugador_nombre)
    print (intentos_por_nivel_quimica)
    nombre= Usuarios.objects.filter(nombre = jugador_nombre).first()
    print(nombre)
    print("La linea 151 esta corriendo")
    resultados = MinijuegoQuimica.objects.create(intentos_por_nivel_quimica=intentos_por_nivel_quimica, tiempo_jugado_quimica=tiempo_jugado_quimica, nivel_actual_quimica=nivel_actual_quimica, scoreQuimica=scoreQuimica, nombre = nombre)
    print (resultados)
    print("Resultado corre bien")
   #resultados.save()
    print("Se realizo el save")
    #nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    retorno = {"EnvioConExito":True}
    return JsonResponse(retorno)

@csrf_exempt
def DatosCompu(request):
    print("Este es el body: ")
    print(request.body)
    print("antes del decode")
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    print("Antes del load")
    body_json = loads(body_unicode)
    print("despues del decode")
    jugador_nombre = body_json['nombre']
    intentos_por_nivel_compu = body_json['intentos_por_nivel_compu']
    tiempo_jugado_compu = body_json['tiempo_jugado_compu']
    nivel_actual_compu = body_json['nivel_actual_compu']
    scoreCompu = body_json['scoreCompu']
    print (jugador_nombre)
    print (intentos_por_nivel_compu)
    nombre= Usuarios.objects.filter(nombre = jugador_nombre).first()
    print(nombre)
    print("La linea 151 esta corriendo")
    resultados = MinijuegoCompu.objects.create(intentos_por_nivel_compu=intentos_por_nivel_compu, tiempo_jugado_compu=tiempo_jugado_compu, nivel_actual_compu=nivel_actual_compu, scoreCompu=scoreCompu, nombre = nombre)
    print (resultados)
    print("Resultado corre bien")
   #resultados.save()
    print("Se realizo el save")
    #nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    retorno = {"EnvioConExito":True}
    return JsonResponse(retorno)

@csrf_exempt
def DatosFisica(request):
    print("Este es el body: ")
    print(request.body)
    print("antes del decode")
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    print("Antes del load")
    body_json = loads(body_unicode)
    print("despues del decode")
    jugador_nombre = body_json['nombre']
    intentos_por_nivel_fisica = body_json['intentos_por_nivel_fisica']
    tiempo_jugado_fisica = body_json['tiempo_jugado_fisica']
    nivel_actual_fisica = body_json['nivel_actual_fisica']
    scoreFisica = body_json['scoreFisica']
    print (jugador_nombre)
    print (intentos_por_nivel_fisica)
    nombre= Usuarios.objects.filter(nombre = jugador_nombre).first()
    print(nombre)
    print("La linea 151 esta corriendo")
    resultados = MinijuegoFisica.objects.create(intentos_por_nivel_fisica=intentos_por_nivel_fisica, tiempo_jugado_fisica=tiempo_jugado_fisica, nivel_actual_fisica=nivel_actual_fisica, scoreFisica=scoreFisica, nombre = nombre)
    print (resultados)
    print("Resultado corre bien")
   #resultados.save()
    print("Se realizo el save")
    #nombre = resultados[0].nombre
    #score = resultados[0].minutos_jugados
    retorno = {"EnvioConExito":True}
    return JsonResponse(retorno)

@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    edad = resultados[0].edad
    genero = resultados[0].genero
    area_fav = resultados[0].area_fav
    usx = User.objects.get(username=usuario)
    last_login = usx.last_login
    #xuser = Usuarios.objects.get(nombre=usuario)
    #last_login = xuser.last_login
    if area_fav == "Quimica":
        carreras = "Químico Farmacobiólogo, Biotecnología"
    elif area_fav == "Fisica":
        carreras = "Mecatrónica, Astrónomo, Robótica"
    else:
        carreras = "ITC, Ciberseguridad, Videojuegos"
    return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"edad":edad, "genero":genero, "carreras":carreras, "last_login":last_login})

def EstadisticasGlobales(request):
    #Inica grafica de tiempo jugado
    data = [['','', '{}']]
   
    resultados = Usuarios.objects.all()
    quimica = MinijuegoQuimica.objects.all()
    fisica = MinijuegoFisica.objects.all()
    compu = MinijuegoCompu.objects.all()


    nombre = resultados[0].nombre
    #minutos_jugados = resultados[0].minutos_jugados

    for i in quimica:
        segundos_q = i.tiempo_jugado_quimica
    
    for j in fisica:
        segundos_f = j.tiempo_jugado_fisica
    
    for k in compu:
        segundos_c = k.tiempo_jugado_compu
    
    data.append(['Quimica', segundos_q, 'color: #b0120a'])
    data.append(['Fisica', segundos_f, 'color: #004411'])
    data.append(['Compu', segundos_c, 'color: #ffab91'])
    
    datos_formato=dumps(data)
    titulo='Indicadores STEM'
    subtitulo='Tiempo jugado'
    titulo_formato = dumps(titulo)
    subtitulo_formato =dumps(subtitulo)
    #Termina grafica de barras minutos jugados


    #Inicia grafica de pastel de edad
    data1=[['Edad','Número personas']]
    edad = resultados[0].edad
    menores_12=0
    entre_1218=0
    mayores18 =0
    for i in resultados:
        if(i.edad < 12):
            menores_12 += 1
        elif(i.edad > 12 and i.edad < 18):
            entre_1218 += 1
        else:
            mayores18 += 1
    data1.append(['<12',menores_12])
    data1.append(['entre 12 y 18',entre_1218])
    data1.append(['mayores 18',mayores18])
    datos_formato1=dumps(data1)
    titulo1='Indicadores STEM'
    subtitulo1='Edades'
    titulo_formato1 = dumps(titulo1)
    subtitulo_formato1 =dumps(subtitulo1)
    #Termina grafica de pastel de edades
    
    #Inicia grafica de barras topscore de cada juego
    data2 = [[' ','Score']]
   
    resultados = Usuarios.objects.all()
    nombre = resultados[0].nombre
    #scores=quimica[0].scoreQuimica
    nombre1 = quimica[0].nombre
    topQ= 0
    topF = 0
    topC = 0
    for i in quimica:
        topQ = max(topQ,i.scoreQuimica)

    for k in fisica:
        topF = max(topF,k.scoreFisica)
        
    for l in compu:
        topC = max(topC,l.scoreCompu)

    data2.append(['Mezclas',topQ])
    data2.append(['Math Runner',topC])
    data2.append(['Básquetbol',topF])

    #topQ = max()
    #topF = max(resultados.scoreFisica)
    #topC = max(resultados.scoreCompu)
        
    #data2.append(['Mezclas',topQ])
    #data2.append(['MathCube',topC])
    #data2.append(['Basquet',topF])
    datos_formato2=dumps(data2)
    titulo2='Indicadores STEM'
    subtitulo2='Score'
    titulo_formato2 = dumps(titulo2)
    subtitulo_formato2 =dumps(subtitulo2)

    #Finn de grafica de barras topscore cada juego


    #Inicio de grafica de dona de genero
    data3=[['Genero','Número personas']]
    genero = resultados[0].genero
    hombres=0
    mujeres=0

    for i in resultados:
        if(i.genero == 'Masculino'):
            hombres += 1
        else:
            mujeres += 1

    data3.append(['Hombres',hombres])
    data3.append(['Mujeres',mujeres])
    datos_formato3=dumps(data3)
    titulo3='Indicadores STEM'
    subtitulo3='Generos'
    titulo_formato3 = dumps(titulo3)
    subtitulo_formato3 =dumps(subtitulo3)

    #Termino de grafica de dona de genero


    #Inicio de grafica de dona permanencia mayor a 10 min en juego fisica
    data4=[['Genero','Número personas']]
    genero2 = resultados[0].genero
    hombres10=0
    mujeres10=0
    for i in quimica:
        if(i.tiempo_jugado_quimica<100):
            if(i.nombre.genero == 'Masculino'):
                hombres10 += 1
            else:
                mujeres10 += 1

    for l in fisica:
        if(l.tiempo_jugado_fisica<100):
            if(l.nombre.genero == 'Masculino'):
                hombres10 += 1
            else:
                mujeres10 += 1

    for r in compu:
        if(r.tiempo_jugado_compu<100):
            if(r.nombre.genero == 'Masculino'):
                hombres10 += 1
            else:
                mujeres10 += 1


    data4.append(['Hombres',hombres10])
    data4.append(['Mujeres',mujeres10])
    datos_formato4=dumps(data4)
    titulo4='Indicadores STEM'
    subtitulo4='Más de 10 min jugando'
    titulo_formato4 = dumps(titulo4)
    subtitulo_formato4 =dumps(subtitulo4)

    #Termina grafica de dona permanencia mayor a 10 min en juego fisica


    #Inicia grafica de dona permanencia total por genero en el juego
    data5=[['Genero','Número personas']]
    genero3 = resultados[0].genero
    tiempoTHombres= 0
    tiempoTMujeres = 0

    for q in quimica:
        if(q.nombre.genero == 'Masculino'):
            tiempoTHombres = tiempoTHombres + q.tiempo_jugado_quimica
        else:
            tiempoTMujeres= tiempoTMujeres + q.tiempo_jugado_quimica

    for w in fisica:
        if(w.nombre.genero == 'Masculino'):
            tiempoTHombres = tiempoTHombres + w.tiempo_jugado_fisica
        else:
            tiempoTMujeres= tiempoTMujeres + w.tiempo_jugado_fisica

    for e in compu:
        if(e.nombre.genero == 'Masculino'):
            tiempoTHombres = tiempoTHombres + e.tiempo_jugado_compu
        else:
            tiempoTMujeres= tiempoTMujeres + e.tiempo_jugado_compu

    data5.append(['Permanencia en línea Hombres',tiempoTHombres])
    data5.append(['Permanencia en línea Mujeres',tiempoTMujeres])
    datos_formato5=dumps(data5)
    titulo5='Indicadores STEM'
    subtitulo5='Permanencia en linea por genero'
    titulo_formato5 = dumps(titulo5)
    subtitulo_formato5 =dumps(subtitulo5)

    #Termina grafica de dona permanencia total por genero en el juego


    #Empieza grafica de barras de promedio de tiempo por juego
    data6=[[' ','Tiempo']]
    genero4 = resultados[0].genero
    tiempoQ= 0
    tiempoF= 0
    tiempoC = 0
    tiempoT = 0
    contQ=0
    contF=0
    contC=0
  

    for t in quimica:
        tiempoQ = t.tiempo_jugado_quimica + tiempoQ
        contQ += 1
    tiempoQ = tiempoQ /contQ

    for y in fisica:
        tiempoF = y.tiempo_jugado_fisica + tiempoF
        contF += 1
    tiempoF = tiempoF /contF

    for o in compu:
        tiempoC = o.tiempo_jugado_compu + tiempoC
        contC += 1
    tiempoC = tiempoC /contC

    data6.append(['Mezclas',tiempoQ])
    data6.append(['Math Runner',tiempoC])
    data6.append(['Básquetbol',tiempoF])
    datos_formato6=dumps(data6)
    titulo6='Indicadores STEM'
    subtitulo6='Tiempo promedio por juego'
    titulo_formato6 = dumps(titulo6)
    subtitulo_formato6 =dumps(subtitulo6)

    #termina grafica de barras de promedio de tiempo por juego


    #Inicia grafica de barras de top 5 scores juego fisica
    data7=[[' ','Score']]
    arr = [0,0,0,0,0]

    for h in fisica:
        #arr=h.scoreFisica
        arr.append(h.scoreFisica)
    srt = sorted(arr, reverse=True)


    data7.append(['Puesto 1',srt[0]])
    data7.append(['Puesto 2',srt[1]])
    data7.append(['Puesto 3',srt[2]])
    data7.append(['Puesto 4',srt[3]])
    data7.append(['Puesto 5',srt[4]])
    datos_formato7=dumps(data7)
    titulo7='Indicadores STEM'
    subtitulo7='Tiempo promedio por juego'
    titulo_formato7 = dumps(titulo7)
    subtitulo_formato7 =dumps(subtitulo7)

    #Termina grafica de barras de top 5 score juego fisica

    #Inica grafica de barras de top 5 score juego quimica
    data8=[[' ','Score']]
    arr = [0,0,0,0,0]


    for f in quimica:
        #arr=h.scoreFisica
        arr.append(f.scoreQuimica)
    srt = sorted(arr, reverse=True)


    data8.append(['Puesto 1',srt[0]])
    data8.append(['Puesto 2',srt[1]])
    data8.append(['Puesto 3',srt[2]])
    data8.append(['Puesto 4',srt[3]])
    data8.append(['Puesto 5',srt[4]])
    datos_formato8=dumps(data8)
    titulo8='Indicadores STEM'
    subtitulo8='Tiempo promedio por juego'
    titulo_formato8 = dumps(titulo8)
    subtitulo_formato8 =dumps(subtitulo8)

    #Termina grafica de barras de top 5 score juego quimica


    #Inica grafica de barras de top 5 score juego compu

    data9=[[' ','Score']]
    arr = [0,0,0,0,0]


    for c in compu:
        #arr=h.scoreFisica
        arr.append(c.scoreCompu)
    srt = sorted(arr, reverse=True)


    data9.append(['Puesto 1',srt[0]])
    data9.append(['Puesto 2',srt[1]])
    data9.append(['Puesto 3',srt[2]])
    data9.append(['Puesto 4',srt[3]])
    data9.append(['Puesto 5',srt[4]])
    datos_formato9=dumps(data9)
    titulo9='Indicadores STEM'
    subtitulo9='Tiempo promedio por juego'
    titulo_formato9 = dumps(titulo9)
    subtitulo_formato9 =dumps(subtitulo9)

    #Termina grafica de barras de top5  score juego compu

    #Inicia grafica de barras de max y min de tiempos
    data10=[['Minijuego','Mínimo','Máximo']]
    arr = [0,0,0,0,0]

    minQuimica = 1000
    maxQuimica = 0
    minFisica = 1000
    maxFisica = 0
    minCompu = 1000
    maxCompu = 0

    for n in quimica:
        #arr=h.scoreFisica
        minQuimica = min(minQuimica,n.tiempo_jugado_quimica)
        maxQuimica = max(maxQuimica,n.tiempo_jugado_quimica)

    for k in fisica:
        #arr=h.scoreFisica
        minFisica = min(minFisica,k.tiempo_jugado_fisica)
        maxFisica = max(maxFisica,k.tiempo_jugado_fisica)

    for t in compu:
        #arr=h.scoreFisica
        minCompu = min(minCompu,t.tiempo_jugado_compu)
        maxCompu = max(maxCompu,t.tiempo_jugado_compu)


    data10.append(['Mezclas',minQuimica, maxQuimica])
    data10.append(['MathCube',minCompu, maxCompu])
    data10.append(['Básquetbol',minFisica,maxFisica])

    datos_formato10=dumps(data10)
    titulo10='Indicadores STEM'
    subtitulo10='Tiempo promedio por juego'
    titulo_formato10 = dumps(titulo10)
    subtitulo_formato10 =dumps(subtitulo10)
    #return render(request, 'Estadisticas.html', {"nombreUsuario":nombre,"edad":edad, "genero":genero, "carreras":carreras})
    return render(request, 'EstadisticasGlobales.html',{'losDatos':datos_formato,'losDatos1':datos_formato1,'losDatos2':datos_formato2,'losDatos3':datos_formato3,'losDatos4':datos_formato4,'losDatos5':datos_formato5,'losDatos6':datos_formato6,'losDatos7':datos_formato7,'losDatos8':datos_formato8,'losDatos9':datos_formato9,'losDatos10':datos_formato10,
    'titulo':titulo_formato,'titulo1':titulo_formato1,'titulo2':titulo_formato2,'titulo3':titulo_formato3,'titulo4':titulo_formato4,'titulo5':titulo_formato5,'titulo6':titulo_formato6,'titulo7':titulo_formato7,'titulo8':titulo_formato8,'titulo9':titulo_formato9,'titulo10':titulo_formato10,
    'subtitulo':subtitulo_formato,'subtitulo1':subtitulo_formato1,'subtitulo2':subtitulo_formato2,'subtitulo3':subtitulo_formato3,'subtitulo4':subtitulo_formato4,'subtitulo5':subtitulo_formato5,'subtitulo6':subtitulo_formato6,'subtitulo7':subtitulo_formato7,'subtitulo8':subtitulo_formato8,'subtitulo9':subtitulo_formato9,'subtitulo10':subtitulo_formato10})

 
"""@login_required
def Estadisticas(request):
    usuario = request.user
    resultados = Usuarios.objects.filter(nombre=usuario)
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

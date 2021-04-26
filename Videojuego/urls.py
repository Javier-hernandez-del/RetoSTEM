from django.urls import path, include
from . import views
"""urlpatterns = [
    path('',views.index, name = 'index'),
    path('proceso', views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
]"""

urlpatterns = [
    #path('',views.index, name = 'index'),
    path('GAMESTEAM',views.GAMESTEAM, name = 'GAMESTEAM'),
    path('Estadisticas',views.Estadisticas, name = 'Estadisticas'),
    path('EstadisticasGlobales',views.EstadisticasGlobales, name = 'EstadisticasGlobales'),
    path('datos',views.datos, name = 'datos'),
    path('unity',views.unity, name = 'unity'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('accounts/register/', views.register, name='register'),
    path('nomatch', views.nomatch, name='nomatch'),
    path('nuevo_usuario',views.nuevo_usuario, name = 'nuevo_usuario'),
    path('grafica',views.grafica, name = 'grafica'),
    path('barras',views.barras, name = 'barras'),
    path('login_unity',views.login_unity, name = 'login_unity'),
    path('buscaJugadorBodyQuimca',views.buscaJugadorBodyQuimca, name = 'buscaJugadorBodyQuimca'),
    path('DatosFisica',views.DatosFisica, name = 'DatosFisica'),
    path('DatosCompu',views.DatosCompu, name = 'DatosCompu'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    #path('GAMESTEAM/', include('django.contrib.auth.urls')),
]


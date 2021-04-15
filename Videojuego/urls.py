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
    path('datos',views.datos, name = 'datos'),
    path('unity',views.unity, name = 'unity'),
    path('buscaJugadorBody',views.buscaJugadorBody, name = 'buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('accounts/register/', views.register, name='register'),
    #path('score',views.score, name = 'score'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    #path('GAMESTEAM/', include('django.contrib.auth.urls')),
]


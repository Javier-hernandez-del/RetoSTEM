from django.urls import path
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
    #path('datos2',views.datos2, name = 'datos2'),
]

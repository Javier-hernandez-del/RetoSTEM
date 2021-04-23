from django.contrib import admin
from . models import Usuarios
from . models import Edades
from . models import PermanenciaEnLinea
from . models import MinijuegoCompu, MinijuegoFisica, MinijuegoQuimica
#from django.db.models import get_models, get_app

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Edades)
admin.site.register(PermanenciaEnLinea)
admin.site.register(MinijuegoCompu)
admin.site.register(MinijuegoFisica)
admin.site.register(MinijuegoQuimica)

#for model in get_models(get_app('Videojuego')):
#    admin.site.register(model)
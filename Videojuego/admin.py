from django.contrib import admin
from . models import Usuarios
from . models import Edades
from . models import PermanenciaEnLinea

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Edades)
admin.site.register(PermanenciaEnLinea)
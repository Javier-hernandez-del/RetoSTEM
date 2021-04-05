from django.contrib import admin
from . models import Usuarios
from . models import Edades

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Edades)
from django.contrib import admin
from .models import Servicio, Articulo, Cliente, Tutorial, Plantilla

admin.site.register(Servicio)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Tutorial)
admin.site.register(Plantilla)
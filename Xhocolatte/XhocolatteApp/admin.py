from django.contrib import admin
from .models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido1' , 'correo']
    list_display = ('nombre', 'apellido1', 'email', 'direccion', 'estado', 'fecha_creacion',)


class PagoAdmin(admin.ModelAdmin):
    search_fields = ['titular','numeroTarjeta']
    list_display = ('titular', 'numeroTarjeta','caducidad_tarjeta', 'cliente',)

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Pago,PagoAdmin)
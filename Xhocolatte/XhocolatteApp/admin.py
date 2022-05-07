from django.contrib import admin
from .models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido1' , 'correo']
    list_display = ('nombre', 'apellido1', 'email', 'direccion', 'estado', 'fecha_creacion',)


class PagoAdmin(admin.ModelAdmin):
    search_fields = ['titular','numeroTarjeta']
    list_display = ('titular', 'numeroTarjeta','caducidad_tarjeta', 'cliente',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio', 'en_stock', 'fecha_creacion']
    list_editable = ['precio', 'en_stock']
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Pago,PagoAdmin)
admin.site.register(Empleado)
admin.site.register(Encargo)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Produccion)
admin.site.register(ProductoEncargo)
admin.site.register(Funcion)
admin.site.register(Receta)
admin.site.register(Inventario)
admin.site.register(InventarioReceta)
admin.site.register(Proveedor)
admin.site.register(ProveedoresInventario)
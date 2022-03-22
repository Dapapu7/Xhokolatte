from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Cliente', max_length = 50, null = False, blank = False)
    apellido1 = models.CharField('Primer apellido del Cliente', max_length = 30, null = False, blank = False)
    apellido2 = models.CharField('Segundo apellido del Cliente', max_length = 30, null = True, blank = True)
    email = models.EmailField('Gmail', blank = False, null = False)
    direccion = models.CharField('Dirección', max_length = 255, null = False, blank = False)
    telefono = models.CharField('Teléfono', max_length = 9, blank = False, null = False)
    cod_postal = models.CharField('Código Postal', max_length = 5, null = False, blank = False)
    estado = models.BooleanField('Cliente Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return "{0},{1}".format(self.apellido1, self.nombre)


class Pago(models.Model):
    id = models.AutoField(primary_key = True)
    titular = models.CharField('Titular de la Tarjeta', max_length = 255, blank = False, null = False)
    numeroTarjeta = models.CharField('Número de la Tarjeta', max_length = 16, blank = False, null = False)
    ccv = models.CharField('CCV', max_length = 3, blank = False, null = False)
    caducidad_tarjeta = models.DateField('Caducidad', null = False, blank = False)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    estado = models.BooleanField('Cliente Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return self.numeroTarjeta


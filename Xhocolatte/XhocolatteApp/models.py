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
    estado = models.BooleanField('Pago Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return self.numeroTarjeta


class Empleado(models.Model):
    id = models.AutoField(primary_key = True)
    dni = models.CharField('DNI', max_length = 9, null = False, blank = False)
    nombre = models.CharField('Nombre del Cliente', max_length = 50, null = False, blank = False)
    apellido1 = models.CharField('Primer apellido del Cliente', max_length = 30, null = False, blank = False)
    apellido2 = models.CharField('Segundo apellido del Cliente', max_length = 30, null = True, blank = True)
    email = models.EmailField('Gmail', blank = False, null = False)
    direccion = models.CharField('Dirección', max_length = 255, null = False, blank = False)
    telefono = models.CharField('Teléfono', max_length = 9, blank = False, null = False)
    estado = models.BooleanField('Empleado Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return "{0},{1}".format(self.apellido1, self.nombre)


class Encargo(models.Model):
    id = models.AutoField(primary_key = True)
    fechaEncargo = models.DateTimeField('Fecha de Encargo', blank = False, null = False)
    fechaEntrega = models.DateTimeField('Fecha de Entrega', blank = True, null = True)
    recibido = models.BooleanField('Recibido', default = False)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    estado = models.BooleanField('Encargo Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Encargo'
        verbose_name_plural = 'Encargos'

    def __str__(self):
        return "{0},{1}".format(self.id, self.fechaEncargo)


class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('Descripción', max_length = 255, blank = False, null = False)
    existencias = models.IntegerField('Existencias', blank = False, null = False)
    precio = models.FloatField('Precio', blank = False, null = False)
    encargo = models.ManyToManyField(Encargo)
    estado = models.BooleanField('Producto Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.descripcion


class Produccion(models.Model):
    id = models.AutoField(primary_key = True)
    cantidad = models.IntegerField('Cantidad', blank = False, null = False)
    costoProduccion = models.FloatField('Coste Producción', blank = False, null = False)
    costesIndirectos = models.FloatField('Costes Indirectos', blank = False, null = False)
    ganancias = models.FloatField('Ganancias', blank = False, null = False)
    fecha = models.DateTimeField('Fecha', blank = False, null = False)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    estado = models.BooleanField('Producción Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Produccion'
        verbose_name_plural = 'Producciones'

    def __str__(self):
        return "{0},{1},{2}".format(self.id, self.fecha, self.producto)

class ProductoEncargo(models.Model):
    id = models.AutoField(primary_key = True)
    cantidad = models.IntegerField('Cantidad del Encargo', blank = False, null = False)
    precio = models.FloatField('Precio', blank = False, null = False)
    producto_id = models.ForeignKey(Producto, on_delete = models.CASCADE)
    encargo_id = models.ForeignKey(Encargo, on_delete = models.CASCADE)
    estado = models.BooleanField('DetalleEncargo Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'detalleEncargo'
        verbose_name_plural = 'detalleEncargos'

    def __str__(self):
        return self.id
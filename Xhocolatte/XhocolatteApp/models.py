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


class Funcion(models.Model):
    id = models.AutoField(primary_key = True)
    cargo = models.CharField('Cargo', max_length = 100, blank = False, null = False)
    empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    estado = models.BooleanField('Cargo Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Funcion'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return self.cargo


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
    imagen = models.ImageField(null = True, blank = True, upload_to = 'productos')
    existencias = models.IntegerField('Existencias', blank = False, null = False)
    precio = models.FloatField('Precio', blank = False, null = False)
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


class Receta(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 45, blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length = 255, blank = False, null = False)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    estado = models.BooleanField('Receta Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('Descripción', max_length = 255, blank = False, null = False)
    unidad = models.CharField('Unidad', max_length = 45, blank = False, null = False)
    precio = models.FloatField('Precio', blank = False, null = False)
    cantidad = models.IntegerField('Cantidad', blank = False, null = False)
    receta = models.ManyToManyField(Receta)
    estado = models.BooleanField('Receta Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return self.descripcion


class InventarioReceta(models.Model):
    id = models.AutoField(primary_key = True)
    ingrediente = models.CharField('Ingredientes', max_length = 45, blank = False, null = False)
    cantidad = models.CharField('Cantidad', max_length = 45, blank = False, null = False)
    unidad_medida = models.CharField('Unidad de medida', max_length = 45, blank = False, null = False)
    receta_id = models.ForeignKey(Receta, on_delete = models.CASCADE)
    inventario_id = models.ForeignKey(Inventario, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'listaIngrediente'
        verbose_name_plural = 'listaIngredientes'

    def __str__(self):
        return self.ingrediente

    
class Proveedor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100, blank = False, null = False)
    telefono = models.CharField('Teléfono', max_length = 9, blank = False, null = False)
    inventario = models.ManyToManyField(Inventario)
    estado = models.BooleanField('Receta Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return "{0},{1}".format(self.nombre, self.telefono)


class ProveedoresInventario(models.Model):
    id = models.AutoField(primary_key = True)
    inventario_id = models.ForeignKey(Inventario, on_delete = models.CASCADE)
    proveedor_id = models.ForeignKey(Proveedor, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'proveedorInventario'
        verbose_name_plural = 'proveedoresInventario'

    def __str__(self):
        return "{0},{1},{2}".format(self.id, self.inventario_id, self.proveedor_id)
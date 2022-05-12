# Generated by Django 4.0.4 on 2022-05-12 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Cliente')),
                ('apellido1', models.CharField(max_length=30, verbose_name='Primer apellido del Cliente')),
                ('apellido2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo apellido del Cliente')),
                ('email', models.EmailField(max_length=254, verbose_name='Gmail')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('cod_postal', models.CharField(max_length=5, verbose_name='Código Postal')),
                ('estado', models.BooleanField(default=True, verbose_name='Cliente Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=9, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Cliente')),
                ('apellido1', models.CharField(max_length=30, verbose_name='Primer apellido del Cliente')),
                ('apellido2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo apellido del Cliente')),
                ('email', models.EmailField(max_length=254, verbose_name='Gmail')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('estado', models.BooleanField(default=True, verbose_name='Empleado Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Encargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaEncargo', models.DateTimeField(verbose_name='Fecha de Encargo')),
                ('fechaEntrega', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Entrega')),
                ('recibido', models.BooleanField(default=False, verbose_name='Recibido')),
                ('estado', models.BooleanField(default=True, verbose_name='Encargo Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.empleado')),
            ],
            options={
                'verbose_name': 'Encargo',
                'verbose_name_plural': 'Encargos',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('unidad', models.CharField(max_length=45, verbose_name='Unidad')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('estado', models.BooleanField(default=True, verbose_name='Receta Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.TextField(default='Que rico esta esto', verbose_name='Descripción')),
                ('alergenos', models.TextField(default='Ninguno', verbose_name='Alergenos')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('existencias', models.IntegerField(verbose_name='Existencias')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('slug', models.SlugField(max_length=255)),
                ('en_stock', models.BooleanField(default=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Producto Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('estado', models.BooleanField(default=True, verbose_name='Receta Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('inventario', models.ManyToManyField(to='XhocolatteApp.inventario')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('estado', models.BooleanField(default=True, verbose_name='Receta Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.producto')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='ProveedoresInventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inventario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.inventario')),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.proveedor')),
            ],
            options={
                'verbose_name': 'proveedorInventario',
                'verbose_name_plural': 'proveedoresInventario',
            },
        ),
        migrations.CreateModel(
            name='ProductoEncargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(verbose_name='Cantidad del Encargo')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('estado', models.BooleanField(default=True, verbose_name='DetalleEncargo Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('encargo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.encargo')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.producto')),
            ],
            options={
                'verbose_name': 'detalleEncargo',
                'verbose_name_plural': 'detalleEncargos',
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('costoProduccion', models.FloatField(verbose_name='Coste Producción')),
                ('costesIndirectos', models.FloatField(verbose_name='Costes Indirectos')),
                ('ganancias', models.FloatField(verbose_name='Ganancias')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('estado', models.BooleanField(default=True, verbose_name='Producción Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.producto')),
            ],
            options={
                'verbose_name': 'Produccion',
                'verbose_name_plural': 'Producciones',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titular', models.CharField(max_length=255, verbose_name='Titular de la Tarjeta')),
                ('numeroTarjeta', models.CharField(max_length=16, verbose_name='Número de la Tarjeta')),
                ('ccv', models.CharField(max_length=3, verbose_name='CCV')),
                ('caducidad_tarjeta', models.DateField(verbose_name='Caducidad')),
                ('estado', models.BooleanField(default=True, verbose_name='Pago Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.cliente')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='InventarioReceta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingrediente', models.CharField(max_length=45, verbose_name='Ingredientes')),
                ('cantidad', models.CharField(max_length=45, verbose_name='Cantidad')),
                ('unidad_medida', models.CharField(max_length=45, verbose_name='Unidad de medida')),
                ('inventario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.inventario')),
                ('receta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.receta')),
            ],
            options={
                'verbose_name': 'listaIngrediente',
                'verbose_name_plural': 'listaIngredientes',
            },
        ),
        migrations.AddField(
            model_name='inventario',
            name='receta',
            field=models.ManyToManyField(to='XhocolatteApp.receta'),
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('estado', models.BooleanField(default=True, verbose_name='Cargo Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.empleado')),
            ],
            options={
                'verbose_name': 'Funcion',
                'verbose_name_plural': 'Funciones',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Required', verbose_name='Description')),
                ('slug', models.SlugField(max_length=255)),
                ('regular_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular price')),
                ('discount', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount price')),
                ('is_active', models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product Specification',
                'verbose_name_plural': 'Product Specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, unique=True, verbose_name='Product Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product Type',
                'verbose_name_plural': 'Product Types',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Product specification value (maximum of 255 words)', max_length=255, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='XhocolatteApp.product')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='XhocolatteApp.productspecification')),
            ],
            options={
                'verbose_name': 'Product Specification Value',
                'verbose_name_plural': 'Product Specification Values',
            },
        ),
        migrations.AddField(
            model_name='productspecification',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='XhocolatteApp.producttype'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Upload a product image', upload_to='images/', verbose_name='Image')),
                ('alt_text', models.CharField(blank=True, help_text='Please add alternative text', max_length=255, null=True, verbose_name='Alternative text')),
                ('is_feature', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='XhocolatteApp.product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='XhocolatteApp.producttype'),
        ),
    ]

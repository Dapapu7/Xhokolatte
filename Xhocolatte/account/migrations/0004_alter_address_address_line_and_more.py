# Generated by Django 4.0.4 on 2022-05-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customer_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line',
            field=models.CharField(max_length=255, verbose_name='Dirección 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line2',
            field=models.CharField(max_length=255, verbose_name='Dirección 2'),
        ),
        migrations.AlterField(
            model_name='address',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=9, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=5, verbose_name='Código Postal'),
        ),
        migrations.AlterField(
            model_name='address',
            name='town_city',
            field=models.CharField(max_length=150, verbose_name='Ciudad'),
        ),
    ]

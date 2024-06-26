# Generated by Django 5.0.3 on 2024-04-04 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_producto',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('ape_paterno', models.CharField(max_length=200)),
                ('ape_materno', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('correo_electronico', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('ape_paterno', models.CharField(max_length=200)),
                ('ape_materno', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('correo_electronico', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('correo_electronico', models.CharField(max_length=200)),
                ('informacion_extra', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagenUrl', models.ImageField(upload_to='imagenesProductos')),
                ('stock', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.categoria_producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('FK_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_venta',
            fields=[
                ('id_detalle_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_producto', models.IntegerField(default=1)),
                ('Fk_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.producto')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.venta')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-12 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0004_alter_venta_fk_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='FK_cliente',
        ),
        migrations.DeleteModel(
            name='Detalle_venta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]

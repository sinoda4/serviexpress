# Generated by Django 5.0.6 on 2024-05-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_venta_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado_venta',
            field=models.CharField(choices=[('Exitosa', 'Exitosa'), ('Cancelada', 'Cancelada'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=100),
        ),
    ]

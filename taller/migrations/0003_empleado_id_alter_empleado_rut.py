# Generated by Django 5.0.3 on 2024-04-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0002_alter_cliente_rut_alter_empleado_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rut',
            field=models.IntegerField(),
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from taller.models import Producto

#Import para la senial
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Venta(models.Model):
    ESTADO_VENTA = [
        ('Exitosa', 'Exitosa'),
        ('Cancelada', 'Cancelada'),
        ('Pendiente', 'Pendiente'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    estado_venta = models.CharField(max_length=100, choices=ESTADO_VENTA,default="Pendiente")    
    def __str__(self):
        return f'Orden - {str(self.pk)}'


class Detalle_venta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return f'Orden - {str(self.venta.pk)} |  Detalle venta - {str(self.pk)}'


#Senial post detalle venta
@receiver(post_save, sender=Detalle_venta)
def actualizar_total_venta(sender, instance, **kwargs):
    # Calcular el total de la venta relacionada al detalle actualizado
    venta = instance.venta
    detalles = venta.detalle_venta_set.all()
    total = sum(detalle.producto.precio * detalle.cantidad  for detalle in detalles)
    venta.total = total
    venta.save()
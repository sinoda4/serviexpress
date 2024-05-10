from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    ape_paterno = models.CharField(max_length=200)
    ape_materno = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=200)
    def __str__(self):
        txt = "rut: {0} - nombre: {1} - correo: {2}"
        return txt.format(self.pk, self.nombre,  self.correo_electronico)


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=200)
    informacion_extra = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        txt = "id: {0} - nombre: {1} - correo: {2}"
        return txt.format(self.pk, self.nombre_proveedor, self.correo_electronico)


class Categoria_producto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=200)

    def __str__(self):
        txt = "Categoria: {0}"
        return txt.format(self.nombre_categoria)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)
    imagenUrl = models.ImageField(upload_to="imagenesProductos")
    stock = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)

    def __str__(self):
        txt = "id: {0} - nombre: {1} - precio: {2}"
        return txt.format(self.id_producto, self.nombre_producto, self.precio)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    total = models.IntegerField(default=0, blank=True, null=True)
    fecha_venta = models.DateField(auto_now_add=True)
    FK_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Detalle_venta(models.Model):
    id_detalle_reserva = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Venta, on_delete=models.CASCADE)
    Fk_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(default=1, )

class Empleado(models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=200)
    ape_paterno = models.CharField(max_length=200)
    ape_materno = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=200)
    def __str__(self):
        txt = "rut: {0} - nombre: {1} - correo: {2}"
        return txt.format(self.rut, self.nombre,  self.correo_electronico)
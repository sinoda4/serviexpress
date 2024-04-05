from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import os
from django.conf import settings
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from datetime import datetime, timedelta


def index(request):
    vProductos = Producto.objects.all()[:6]
    template = loader.get_template("taller/index.html")
    context = {"productos": vProductos}

    return HttpResponse(template.render(context, request))


def VerProducto(request, prod_id):
    template = loader.get_template("taller/verProducto.html")
    
    try:
        vProducto = Producto.objects.get(pk=prod_id)
        productos_aleatorios = Producto.objects.order_by('?')[:3]
        context = {"producto": vProducto, "aleatorios": productos_aleatorios}
    except Producto.DoesNotExist:
        raise Http404("Producto no existe")
    return HttpResponse(template.render(context, request))


# CRUD Productos


def crudProductos(request):
    vProductos = Producto.objects.all
    vCategorias = Categoria_producto.objects.all
    template = loader.get_template("taller/crudProductos.html")
    vProveedores = Proveedor.objects.all()
    context = {"productos": vProductos, "categorias": vCategorias, "proveedores": vProveedores}
    return HttpResponse(template.render(context, request))


def eliminarProducto(request, prod_id):
    producto = Producto.objects.get(pk=prod_id)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    messages.warning(request, ("Producto eliminado con exito"))
    return redirect("crudProductos")


def agregarCategoria(request):
    v_nombre = request.POST["txtnombreCategoria"]
    Categoria_producto.objects.create(
        nombre_categoria=v_nombre,
    )
    messages.success(request, ("Categoria agregada con exito"))
    return redirect("crudProductos")


def agregarProducto(request):
    v_categoria = Categoria_producto.objects.get(
        id_categoria=request.POST["cmbCategoria"]
    )
    v_proveedor = Proveedor.objects.get(
        id_proveedor=request.POST["cmbProveedor"]
    )

    v_nombre = request.POST["txtnombre"]
    v_precio = request.POST["txtprecio"]
    v_stock = request.POST["txtStock"]
    v_descripcion = request.POST["txtDescripcion"]
    v_imagen = request.FILES["txtImagen"]

    Producto.objects.create(
        nombre_producto=v_nombre,
        precio=v_precio,
        stock=v_stock,
        descripcion=v_descripcion,
        imagenUrl=v_imagen,
        categoria=v_categoria,
        proveedor = v_proveedor
    )
    messages.success(request, ("Producto agregado con exito"))
    return redirect("crudProductos")


# Editar productos
def editarProducto(request, prod_id):
    if request.method == "POST":
        v_categoria = Categoria_producto.objects.get(
            id_categoria=request.POST["cmbCategoria"]
        )
        v_proveedor = Proveedor.objects.get(
            id_proveedor=request.POST["cmbProveedor"]
        )

        v_sku = request.POST["txtSku"]
        productoBD = Producto.objects.get(pk=v_sku)
        v_nombre = request.POST["txtnombre"]
        v_precio = request.POST["txtprecio"]
        v_stock = request.POST["txtStock"]
        v_descripcion = request.POST["txtDescripcion"]

        try:
            v_imagen = request.FILES["txtImagen"]
            ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
            os.remove(ruta_imagen)
            productoBD.imagenUrl = v_imagen
        except:
            productoBD.imagenUrl = productoBD.imagenUrl

        productoBD.nombre_producto = v_nombre
        productoBD.precio = v_precio
        productoBD.stock = v_stock
        productoBD.descripcion = v_descripcion
        productoBD.categoria = v_categoria
        productoBD.proveedor = v_proveedor

        productoBD.save()
        messages.success(request, ("Producto editado con exito"))
        return redirect("crudProductos")

    else:
        prod = Producto.objects.get(pk=prod_id)
        categorias = Categoria_producto.objects.all()
        proveedores = Proveedor.objects.all()
        template = loader.get_template("taller/editarProducto.html")
        context = {"producto": prod, "categorias": categorias, "proveedores": proveedores}
        return HttpResponse(template.render(context, request))


# Crud empleados


def crudEmpleados(request):
    empleados = Empleado.objects.all()

    return render(request, "taller/crudEmpleados.html", {"empleados": empleados})


def agregarEmpleado(request):

    rut = request.POST["txtRut"]
    nombre = request.POST["txtnombre"]
    ap_paterno = request.POST["txtApPat"]
    ap_materno = request.POST["txtApMat"]
    telefono = request.POST["txtNumero"]
    correo = request.POST["txtCorreo"]

    Empleado.objects.create(
        rut = rut,
        nombre = nombre,
        ape_paterno = ap_paterno,
        ape_materno = ap_materno,
        telefono = telefono,
        correo_electronico = correo
    )

    messages.success(request, ("Empleado agregado con exito"))
    return redirect("crud_empleados")

    


def eliminarEmpleado(request, id):
    Empleado.objects.get(pk=id).delete()
    messages.warning(request, ("Empleado eliminado con exito"))
    return redirect("crud_empleados")


def editarEmpleado(request, id):
    if request.method == "POST":
        empleadoBD = Empleado.objects.get(pk=id)
        nombre = request.POST["txtNombre"]
        ap_paterno = request.POST["txtApPat"]
        ap_materno = request.POST["txtApMat"]
        numero = request.POST["txtNumero"]
        correo = request.POST["txtCorreo"]
        
        empleadoBD.nombre = nombre
        empleadoBD.ape_paterno = ap_paterno
        empleadoBD.ape_materno = ap_materno
        empleadoBD.telefono = numero
        empleadoBD.correo_electronico = correo
        empleadoBD.save()

        messages.success(request, ("Empleado actualizado con exito"))
        return redirect("crud_empleados")
    else:
        empleado = Empleado.objects.get(pk=id)  
        return render(request, "taller/editarEmpleado.html", {"empleado": empleado})
    




# Carrito y realizar compra
def carrito(request):
    template = loader.get_template("taller/carrito.html")
    context = {"hola": False}
    return HttpResponse(template.render(context, request))


def confirmarServicio(request):
    if request.method == "POST":
        data = request.POST.get("mi_dato")
        jdata = json.loads(data)
        
        username = None
        if request.user.is_authenticated:
            username = request.user

        fecha = datetime.now() + timedelta(5)
        print(fecha)

        vReserva = Venta.objects.create(
            FK_cliente = username,
            fecha_realizar = fecha
        )


        for j in jdata:
            vServicio = Producto.objects.get(pk=j['id'])
            Detalle_venta.objects.create(
                id_reserva = vReserva,
                FK_servicio = vServicio
            )
        
        

        return redirect('carrito/servicio_confirmado')
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


# CRUD Proveedor


def crudProveedores(request):
    vProveedores = Proveedor.objects.all
    template = loader.get_template("taller/crudProveedores.html")
    context = {"proveedores": vProveedores}
    return HttpResponse(template.render(context, request))


def agregarProveedor(request):
    v_nombre = request.POST["txtNombreProveedor"]
    v_telefono = request.POST["txtTelefono"]
    v_correo = request.POST["txtCorreo"]
    v_extra = request.POST["txtDatosExtras"]

    Proveedor.objects.create(
        nombre_proveedor=v_nombre,
        telefono=v_telefono,
        correo_electronico=v_correo,
        informacion_extra=v_extra,
    )

    messages.success(request, ("Proveedor agregado con exito"))
    return redirect("crud_proveedores")


def eliminarProveedor(request, prov_id):
    Proveedor.objects.get(pk=prov_id).delete()
    messages.warning(request, ("Proveedor eliminado con exito"))
    return redirect("crud_proveedores")

def editarProveedor(request, prov_id):
    if request.method == "POST":
        nombre = request.POST["txtNombreProveedor"]
        telefono = request.POST["txtTelefono"]
        correo= request.POST["txtCorreo"]
        extra = request.POST["txtDatosExtras"]
        proveedor = Proveedor.objects.get(pk=prov_id)
        proveedor.nombre_proveedor = nombre
        proveedor.telefono = telefono
        proveedor.correo_electronico = correo
        proveedor.informacion_extra = extra
        proveedor.save()
        messages.success(request, ("Proveedor editado correctamente"))
        return redirect("crud_proveedores")

    else:
        proveedor = Proveedor.objects.get(pk=prov_id)
        return render(request, "taller/editarProveedor.html", {"prov": proveedor})


# Inicio de sesion
def ListaProductos(request):
    template = loader.get_template("taller/listaProductos.html")
    vProductos = Producto.objects.all()
    context = {"productos": vProductos}
    return HttpResponse(template.render(context, request))


#Confirmo de servicio
def servicioFinalizado(request):
    template = loader.get_template("taller/confirmoServicio.html")
    username = None
    if request.user.is_authenticated:
        username = request.user
    
    vReserva = Reserva.objects.filter(FK_cliente=username).first()
    vDetalleReserva= Detalle_reserva.objects.all().filter(id_reserva=vReserva)

    print(vReserva)
    print(vDetalleReserva)
    context = {"reserva": vReserva, "detalle": vDetalleReserva  }
    return HttpResponse(template.render(context, request))
    
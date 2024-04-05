from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("producto/<int:prod_id>/", views.VerProducto, name="ventaProducto"),
    # CrudProductos
    path("crud/productos", views.crudProductos, name="crud_productos"),
    path(
        "crud/eliminarProducto/<int:prod_id>",
        views.eliminarProducto,
        name="eliminar_producto",
    ),
    path("crud/agregarProductoForm", views.agregarProducto),
    path(
        "crud/editarProducto/<int:prod_id>",
        views.editarProducto,
        name="editar_producto",
    ),
    
    path("crud/agregarCategoriaForm", views.agregarCategoria, name="agregar_categoria"),
    
    # Crud empleados
    path("crud/empleados", views.crudEmpleados, name="crud_empleados"),
    path("crud/agregarEmpleadoForm", views.agregarEmpleado),
    path(
        "crud/eliminarEmpleado/<int:id>",
        views.eliminarEmpleado,
        name="eliminar_empleado",
    ),
    path(
        "crud/editarEmpleado/<int:id>",
        views.editarEmpleado,
        name="editar_empleado",
    ),
    

    # Compra y carrito
    path("carrito", views.carrito, name="carrito"),
    path("carrito/confirmarServicio", views.confirmarServicio),
    # CRUD Proveedores
    path("crud/proveedores", views.crudProveedores, name="crud_proveedores"),
    
    path("crud/proveedores/agregarProveedorForm", views.agregarProveedor, name="agregar_proveedor"),
    path(
        "crud/proveedores/eliminarProveedor/<int:prov_id>",
        views.eliminarProveedor,
        name="eliminar_proveedor",
    ),
    path(
        "crud/proveedores/editarProveedor/<int:prov_id>",
        views.editarProveedor,
        name="editar_proveedor",
    ),
    #Lista de servicios
    path("productos", views.ListaProductos, name="VerProductos"),
    path("carrito/servicio_confirmado", views.servicioFinalizado),
]

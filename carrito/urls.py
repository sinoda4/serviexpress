from django.urls import path

from . import views


"""
SE VA A REESTRUCTURAR TODO EL CARRITO DE COMPRAS, POR UNA FORMA MAS SENCILLA

"""


urlpatterns =[
      path("", views.carrito, name="carrito"),
      path("realizarCompra", views.realizarCompra, name="realizarCompra"),
      path("add", views.add_carrito, name="add_carrito"),
      path("remove", views.remove_carrito, name="remove-carrito"),
]
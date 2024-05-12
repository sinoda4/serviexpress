from django.urls import path

from . import views


"""
SE VA A REESTRUCTURAR TODO EL CARRITO DE COMPRAS, POR UNA FORMA MAS SENCILLA

"""


urlpatterns =[
      path("", views.carrito, name="carrito"),
      path("realizar_compra", views.realizar_compra, name="realizar_compra"),
      path("add", views.add_carrito, name="add_carrito"),
      path("delete", views.delete_carrito, name="delete_carrito"),
      path("update", views.update_carrito, name="update_carrito"),
      path("payku", views.payku, name="payku")
]
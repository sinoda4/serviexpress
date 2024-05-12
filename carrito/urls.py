from django.urls import path

from . import views


"""
Carrito ya reestructurado :D

"""


urlpatterns =[
      path("", views.carrito, name="carrito"),
      path("add", views.add_carrito, name="add_carrito"),
      path("delete", views.delete_carrito, name="delete_carrito"),
      path("update", views.update_carrito, name="update_carrito"),
      
]
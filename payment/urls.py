from django.urls import path
from . import views




"""
Carrito ya reestructurado :D

"""


urlpatterns =[
      path("", views.payment, name="payment"),
      path("payment_succes", views.payment_succes, name="payment_success"),
      path("checkout", views.checkout, name="payment_checkout"),
      path("sumary", views.sumary, name="payment_sumary"),
      path("payment_process", views.payment_process, name="payment_process"),
      path("payment_payku", views.payku, name="payment_payku"),
]
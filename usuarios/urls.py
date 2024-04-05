from django.urls import path
from . import views


urlpatterns = [
    path("login_usuario", views.login_user, name="login"),
    path("logout_usuario", views.logout_user, name="logout"),
    path("registro_usuario", views.register_user, name="registro_usuario"),
] 

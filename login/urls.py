from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('registrar', views.registrar),
    path('inicio', views.inicio3),
    path('registro', views.registro),
    path('logout', views.logout),
]

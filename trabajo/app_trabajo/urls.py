from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("horarios/", views.horarios, name="horarios"),
    path("estaciones/", views.estaciones, name="estaciones"),
    path("trenes/", views.trenes, name="trenes"),
    path("servicios/", views.servicios, name="servicios"),
    path("reclamos/", views.reclamos, name="reclamos"),
]
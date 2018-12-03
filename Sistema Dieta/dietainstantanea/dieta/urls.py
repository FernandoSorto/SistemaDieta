from django.urls import path
from django.conf.urls import url

from . import views

app_name='dietaApp'

urlpatterns = [
    path('', views.paginaPrincipalDieta, name='paginaPrincipal'),
    path('dietanueva/', views.paginaCrearDieta, name='paginaDieta'),
    path('dietasemanal/', views.paginaDietaSemanal, name='paginaDietaSemanal'),
]

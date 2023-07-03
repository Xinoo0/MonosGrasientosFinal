from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', views.base, name="base"),
    path('inicio/', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('galeria/', views.galeria, name="galeria"),
    
    
    # CONTROL USUARIO Y CUENTAS
    path('login/', views.login, name="login"),
    ]

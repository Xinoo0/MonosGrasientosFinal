from django.urls import path
from . import views
from .views import crud, register
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    #path('', views.base, name="base"),
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('galeria/', views.galeria, name="galeria"),
    
    # CRUD URLS
    path('crud/', views.crud, name='crud'),
    path('agregar/',views.agregar, name='agregar'),
    path('agregarrec/',views.agregarrec,name='agregarrec'),
    path('crud/eliminar/<int:id>/', views.eliminar,name='eliminar'),
    path('crud/actualizar/<int:id>/',views.actualizar,name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/',views.actualizarrec,name='actualizarrec'),
    
    
    # CONTROL USUARIO Y CUENTAS
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]   
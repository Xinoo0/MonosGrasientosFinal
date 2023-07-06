from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=25, blank=False, null=False)
    modelo = models.CharField(max_length=25)
    marca =  models.CharField(max_length=25)
    precio = models.CharField(max_length=10)
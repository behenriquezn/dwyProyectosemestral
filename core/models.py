from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=50,primary_key=True)
    nombresucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    numeroIdentificador= models.IntegerField(blank=True)
    nombre = models.CharField(max_length=12,primary_key=True)
    valor = models.IntegerField()
    notas = models.CharField(max_length=300)
    valorpresupuestado = models.IntegerField()
    tiendanombre = models.CharField(max_length=200,blank=True, null=True)

    objects = models.Manager()
    def __str__(self):
        return self.nombre



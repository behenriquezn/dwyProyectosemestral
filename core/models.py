from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class TipoContacto(models.Model):
    tipoCon = models.CharField(max_length=50)

    def __str__(self):
        return self.tipoCon

class Empleado(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    nombreUsuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    nombreUsuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)

    def __str__(self):
        return self.rut

class Insumo(models.Model):
    nombre = models.CharField(max_length=12)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    stock = models.IntegerField()

    objects = models.Manager()
    def __str__(self):
        return self.nombre


class ContactoFinal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    tipoCon = models.ForeignKey(TipoContacto, on_delete= models.CASCADE)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

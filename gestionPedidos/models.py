from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return 'Nombre: %s, Dirección: %s, Email: %s, Teléfono: %s' % (self.nombre, self.direccion, self.email, self.telefono)


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'Nombre : %s, Sección: %s, Precio: %s' % (self.nombre, self.seccion, self.precio)


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return 'Número: %s, Fecha: %s, Entregado: %s' % (self.numero, self.fecha, self.entregado)

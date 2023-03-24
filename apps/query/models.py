from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Model definition for cliente."""

    cc = models.PositiveBigIntegerField(unique=True)
    nit = models.PositiveBigIntegerField(unique=True)
    pasaporte = models.CharField(max_length=15,unique=True)
    nombre = models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.PositiveBigIntegerField()

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

from django.db import models

# Create your models here.


class Serie(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    capitulos = models.CharField(
        max_length=500, verbose_name="Número de Capítulos")
    emision = models.CharField(max_length=100, verbose_name="Años de Emisión")
    sinopsis = models.TextField(verbose_name="Sinopsis")
    distribuidora = models.CharField(
        max_length=200, verbose_name="Distribuidora")

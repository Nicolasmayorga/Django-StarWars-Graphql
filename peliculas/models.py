from django.db import models

# Create your models here.

"""Este modelo tiene como objetivo la construcción de todos los detalles de cada una de las películas de StarWars desde detalles singulares como su dirección hasta más específicos como presupuesto o fecha de estreno. Esto a través de llaves foraneas permite la construcción de un gran modelo que engloba todos los detalles relevantes de cada una de las películas, además que permite el fácil mantenimiento y escalabilidad de la aplicación de la siguiente manera"""


class Peli(models.Model):
    name = models.CharField(max_length=50, verbose_name="Pelicula")
    director = models.CharField(max_length=100, verbose_name="Director")


class Personaje(models.Model):
    episodio = models.ForeignKey(Peli, on_delete=models.DO_NOTHING)
    Personajes = models.TextField()


class Tecnico(models.Model):
    name = models.ForeignKey(Peli, on_delete=models.DO_NOTHING)
    musica = models.CharField(max_length=500, verbose_name="Música")
    distribuidora = models.CharField(
        max_length=500, verbose_name="Distribuidora")
    estreno = models.CharField(max_length=500, verbose_name="Estreno")
    duracion = models.CharField(max_length=500, verbose_name="Duración")
    presupuesto = models.CharField(max_length=500, verbose_name="Presupuesto")


class Planeta(models.Model):
    name = models.ForeignKey(Peli, on_delete=models.DO_NOTHING)
    planetas = models.CharField(max_length=500, verbose_name="Planetas")


class Resumen(models.Model):
    name = models.ForeignKey(Peli, on_delete=models.DO_NOTHING)
    sinopsis = models.TextField()
    resumen = models.TextField()


class Peliculas(models.Model):
    nombre = models.ForeignKey(Peli, on_delete=models.DO_NOTHING)
    tecnicos = models.ForeignKey(Tecnico, on_delete=models.DO_NOTHING)
    resumen = models.ForeignKey(Resumen, on_delete=models.DO_NOTHING)
    planetas = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING)
    personajes = models.ForeignKey(Personaje, on_delete=models.DO_NOTHING)

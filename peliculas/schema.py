import graphene
from graphene_django import DjangoObjectType
from .models import *

"""Conversión del modelo en objetos a través de una clase para la consecución de un query a través de graphql"""


class PeliType(DjangoObjectType):
    class Meta:
        model = Peli


"""Clase que permite la mutación a través de graphql para la alteración directa del modelo a través de objetos"""


class PeliMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        director = graphene.String(required=True)

    peli = graphene.Field(PeliType)

    def mutate(self, info, id, name, director):
        peli = Peli.objects.get(pk=id)
        peli.name = name
        peli.director = director
        peli.save()
        return PeliMutation(peli=peli)


class Mutation(graphene.ObjectType):
    update_peli = PeliMutation.Field()


class PersonajeType(DjangoObjectType):
    class Meta:
        model = Personaje


class TecnicoType(DjangoObjectType):
    class Meta:
        model = Tecnico


class PlanetaType(DjangoObjectType):
    class Meta:
        model = Planeta


class ResumenType(DjangoObjectType):
    class Meta:
        model = Resumen


class PeliculasType(DjangoObjectType):
    class Meta:
        model = Peliculas


"""Clase Query que permite devolver cada uno de los objetos a través de Graphene en forma de lista"""


class Query(graphene.ObjectType):
    pelis = graphene.List(PeliType)
    personajes = graphene.List(PersonajeType)
    tecnicos = graphene.List(TecnicoType)
    planetas = graphene.List(PlanetaType)
    resumens = graphene.List(ResumenType)
    peliculas = graphene.List(PeliculasType)

    """Funciones de cada uno de los modelos que permiten la consecución de un query a través del frontend"""

    def resolve_pelis(self, info, **kwargs):
        return Peli.objects.all()

    def resolve_personajes(self, info, **kwargs):
        return Personaje.objects.all()

    def resolve_tecnicos(self, info, **kwargs):
        return Tecnico.objects.all()

    def resolve_planetas(self, info, **kwargs):
        return Planeta.objects.all()

    def resolve_resumens(self, info, **kwargs):
        return Resumen.objects.all()

    def resolve_peliculas(self, info, **kwargs):
        return Peliculas.objects.all()

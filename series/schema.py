import graphene
from graphene_django import DjangoObjectType
from .models import *


class SerieType(DjangoObjectType):
    class Meta:
        model = Serie


class Query(graphene.ObjectType):
    series = graphene.List(SerieType)

    def resolve_series(self, info, **kwargs):
        return Serie.objects.all()

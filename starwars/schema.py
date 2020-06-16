import graphene

from series import schema
from peliculas import schema


class Query_Peliculas(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query_Peliculas)


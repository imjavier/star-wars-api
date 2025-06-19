import graphene
from universe.schemas import CharacterQuery, MovieQuery, PlanetQuery

class Query(CharacterQuery, MovieQuery, PlanetQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
import graphene
from universe.schemas import CharacterQuery, MovieQuery, PlanetQuery, CreateMovieMutation

class Query(CharacterQuery, MovieQuery, PlanetQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_movie = CreateMovieMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

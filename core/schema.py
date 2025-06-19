import graphene
from universe.schemas import (
    CharacterQuery,
    MovieQuery,
    PlanetQuery,
    CreateMovieMutation,
    CreateCharacterMutation,
    CreatePlanetMutation
)

class Query(CharacterQuery, MovieQuery, PlanetQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_movie = CreateMovieMutation.Field()
    create_character = CreateCharacterMutation.Field()
    create_planet = CreatePlanetMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

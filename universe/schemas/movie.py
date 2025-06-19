import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from universe.models import Movie
from universe.filters import MovieFilter

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        interfaces = (relay.Node, )
        fields = '__all__'
        filterset_class = MovieFilter

class MovieQuery(ObjectType):
    movie = relay.Node.Field(MovieType)
    all_movies = DjangoFilterConnectionField(
        MovieType
    )

class CreateMovieMutation(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        opening_crawl = graphene.String(required=False)
        director = graphene.String(required=True)
        producers = graphene.String(required=False)
        created_date = graphene.Date(required=True)
        planets = graphene.List(graphene.ID, required=False)
        characters = graphene.List(graphene.ID, required=False)

    movie = graphene.Field(MovieType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        movie = Movie.objects.create(
            title=input.get('title'),
            director=input.get('director'),
            producers=input.get('producers', ''),
            created_date=input.get('created_date'),
        )
        planet_ids = [
            from_global_id(planet)[1]
            for planet in input.get('planets', [])
        ]
        character_ids = [
            from_global_id(character)[1]
            for character in input.get('characters', [])
        ]
        movie.planets.set(planet_ids)
        movie.characters.set(character_ids)

        return CreateMovieMutation(movie=movie)
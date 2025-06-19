import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from universe.models import Movie

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        interfaces = (relay.Node, )
        fields = '__all__'
        filter_fields = {
            'characters__id': ['exact'],
            'title': ['exact', 'icontains'],
        }

class MovieQuery(ObjectType):
    movie = relay.Node.Field(MovieType)
    all_movies = DjangoFilterConnectionField(MovieType)

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
        movie.planets.set(input.get('planets', []))
        movie.characters.set(input.get('characters', []))

        return CreateMovieMutation(movie=movie)
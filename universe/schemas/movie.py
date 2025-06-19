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
        }

class MovieQuery(ObjectType):
    movie = relay.Node.Field(MovieType)
    all_movies = DjangoFilterConnectionField(MovieType)


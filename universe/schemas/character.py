from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from universe.models import Character

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (relay.Node, )
        fields = '__all__'
        filter_fields = {
            'movies__title': ['exact', 'icontains'],
        }

class CharacterQuery(ObjectType):
    character = relay.Node.Field(CharacterType)
    all_characters = DjangoFilterConnectionField(CharacterType)
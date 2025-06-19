import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from universe.schemas import MovieType

from universe.models import Character

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (relay.Node, )
        fields = '__all__'
        filter_fields = {
            'movies__title': ['exact', 'icontains'],
            'name': ['exact', 'icontains']
        }

class CharacterQuery(ObjectType):
    character = relay.Node.Field(CharacterType)
    all_characters = DjangoFilterConnectionField(CharacterType)

class CreateCharacterMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        height = graphene.Float(required=True)

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        character = Character.objects.create(
            name=input.get('name'),
            height=input.get('height')
        )

        return CreateCharacterMutation(character=character)
import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType, DjangoListField

from universe.models import Planet

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        interfaces = (relay.Node, )
        fields = '__all__'


class PlanetQuery(ObjectType):
    planet = relay.Node.Field(PlanetType)
    all_planets = DjangoListField(PlanetType)

class CreatePlanetMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        planet = Planet.objects.create(
            name=input.get('name')
        )

        return CreatePlanetMutation(planet=planet)
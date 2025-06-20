import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from universe.models import Planet

class PlanetType(DjangoObjectType):
    """
    Represents a planet in the Star Wars universe.
    Includes basic information such as the planet's name.
    """
    class Meta:
        model = Planet
        interfaces = (relay.Node, )
        fields = '__all__'
        filter_fields = {
            'name': ['exact', 'icontains']
        }
        description = "A Star Wars planet, containing basic information such as its name."

class PlanetQuery(ObjectType):
    """
    Queries related to planets.
    Allows retrieving a planet by its global ID or listing all planets with filter support.
    """
    planet = relay.Node.Field(
        PlanetType,
        description="Retrieve a planet by its global ID."
    )
    all_planets = DjangoFilterConnectionField(
        PlanetType,
        description="List all Star Wars planets. Supports filters such as name."
    )

class CreatePlanetMutation(relay.ClientIDMutation):
    """
    Mutation to create a new planet in the Star Wars universe.
    """
    class Input:
        name = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        planet = Planet.objects.create(
            name=input.get('name')
        )

        return CreatePlanetMutation(planet=planet)

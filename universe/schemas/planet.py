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

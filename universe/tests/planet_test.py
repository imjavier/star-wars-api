import pytest
from graphene.test import Client
from core.schema import schema

@pytest.mark.django_db
def test_all_character_query(planet):
    client = Client(schema)
    query = '''
        query {
            allPlanets{
                edges{
                    node{
                        name
                    }
                }
            }
        }
    '''
    results = (
        client.execute(query)
        .get('data')
        .get('allPlanets')
        .get('edges')
    )
    names = [result['node']['name'] for result in results]

    assert "Test planet" in names

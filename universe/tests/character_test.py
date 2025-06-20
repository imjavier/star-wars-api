import pytest
from graphene.test import Client
from core.schema import schema

@pytest.mark.django_db
def test_all_character_query(character):
    client = Client(schema)
    query = '''
        query {
            allCharacters {
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
        .get('allCharacters')
        .get('edges')
    )
    names = [result['node']['name'] for result in results]

    assert "Test subject" in names

import pytest
from graphene.test import Client
from universe.models import Movie
from core.schema import schema

@pytest.mark.django_db
def test_all_movies_query(movie):
    client = Client(schema)
    query = '''
        query {
            allMovies {
                edges{
                    node{
                        title
                    }
                }
            }
        }
    '''
    results = (
        client.execute(query)
        .get('data')
        .get('allMovies')
        .get('edges')
    )
    titles = [result['node']['title'] for result in results]

    assert "Test movie" in titles

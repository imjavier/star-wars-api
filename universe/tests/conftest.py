import pytest
from datetime import date
from universe.models import Movie, Character, Planet

@pytest.fixture
def planet():
    return Planet.objects.get_or_create(
        name="Test planet"
    )[0]

@pytest.fixture
def character():
    return Character.objects.get_or_create(
        name="Test subject",
        height=1.9
    )[0]

@pytest.fixture
def movie(planet, character):
    movie = Movie.objects.get_or_create(
        opening_crawl= "First test is being created",
        title="Test movie",
        director="Javier Villarreal",
        producers="1,2",
        created_date=date.today()
    )[0]
    movie.planets.set([planet])
    movie.characters.set([character])

    return movie

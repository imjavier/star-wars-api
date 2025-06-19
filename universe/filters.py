from django_filters import FilterSet
from universe.models import Movie
from helpers.filters import GlobalIDFilter

class MovieFilter(FilterSet):
    id = GlobalIDFilter()  # para permitir id global en allMovies(id: "...")

    characters__id = GlobalIDFilter()  # para permitir filter por character global ID

    class Meta:
        model = Movie
        fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
        }

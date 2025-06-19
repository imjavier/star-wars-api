from django_filters import FilterSet
from universe.models import Movie
from helpers.filters import GlobalIDFilter

class MovieFilter(FilterSet):
    id = GlobalIDFilter()

    characters__id = GlobalIDFilter()

    class Meta:
        model = Movie
        fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains'],
            'characters__name': ['exact', 'icontains']
        }

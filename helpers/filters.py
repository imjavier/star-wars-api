from django_filters import CharFilter
from graphql_relay import from_global_id
from django_filters import CharFilter

class GlobalIDFilter(CharFilter):
    def filter(self, qs, value):
        if value:
            try:
                _, local_id = from_global_id(value)
                return super().filter(qs, local_id)
            except:
                return qs.none()

        return qs

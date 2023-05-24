from django_filters import rest_framework as filters
from .models import Event, Place, User

class EventFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    place_name = filters.CharFilter(field_name='place__name', lookup_expr='icontains')
    user = filters.CharFilter(field_name='user__username', lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['name', 'description', 'place_name', 'user']


class PlaceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    street = filters.CharFilter(lookup_expr='icontains')
    locality = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['name', 'street', 'locality']


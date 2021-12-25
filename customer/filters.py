from django_filters import CharFilter, FilterSet

from .models import Customer


class CustomerFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    nick = CharFilter(lookup_expr='icontains')
    city__city = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['nick', 'name', 'city__city']

        # fields = {
        #     'nick': ['exact', 'icontains'],
        #     'name': ['exact', 'icontains'],
        #     'city__city': ['exact', 'icontains'],
        # }

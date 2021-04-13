from django_filters import FilterSet, CharFilter
from .models import Product


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    # nick = CharFilter(lookup_expr='icontains')
    # city__city = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']
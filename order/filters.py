from django_filters import CharFilter, FilterSet

from .models import Order


class OrderFilter(FilterSet):
    customer__nick = CharFilter(lookup_expr='icontains')
    customer__name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['customer__nick', 'customer__name']

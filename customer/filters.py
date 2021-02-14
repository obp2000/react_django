from django_filters import FilterSet, CharFilter
from django.forms.widgets import TextInput
from .models import Customer


class CustomerFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    nick = CharFilter(lookup_expr='icontains')
    city__city = CharFilter(lookup_expr='icontains', widget=TextInput())

    class Meta:
        model = Customer
        fields = ['nick', 'name']

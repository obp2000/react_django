from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, ChoiceFilter, FilterSet

from .models import Contents, Product


class ProductFilter(FilterSet):
    product_type__name = CharFilter(lookup_expr='icontains')
    contents = ChoiceFilter(choices=Contents.choices,
                            empty_label=_('contents').capitalize())
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['product_type__name', 'contents', 'name']

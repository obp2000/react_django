from django_select2.forms import ModelSelect2Widget

from .models import Product


class ProductWidget(ModelSelect2Widget):
    search_fields = ["name__icontains", "product_type__name__icontains"]
    queryset = Product.objects.select_related('product_type')

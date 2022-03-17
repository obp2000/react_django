"""
API endpoints that allow models to be viewed or edited.
"""
from react_django.api.consts import get_options
from rest_framework.viewsets import ModelViewSet

from ..models import ProductType
from ..views import ProductQuerysetMixin
from .consts_data import consts_data
from .serializers import ProductSerializer, ProductTypeSerializer


class ProductTypeViewSet(ModelViewSet):
    """
    API endpoint that allows product types to be viewed and searched.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    search_fields = ['name']


class ProductViewSet(ProductQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = ProductSerializer
    search_fields = ['name', 'product_type__name', 'price']
    # pagination_class = None
    # page_size = 1000

    def options(self, request, *args, **kwargs):
        return get_options(self, request, consts_data)

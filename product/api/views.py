"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet

from ..models import ProductType
from ..views import ProductListQuerysetMixin
from .serializers import ProductSerializer, ProductTypeSerializer


class ProductTypeViewSet(ModelViewSet):
    """
    API endpoint that allows product types to be viewed and searched.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    search_fields = ['name']


class ProductViewSet(ProductListQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = ProductSerializer
    search_fields = ['name', 'price']
    # pagination_class = None
    # page_size = 1000

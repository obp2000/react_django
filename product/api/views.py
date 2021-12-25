"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet

from ..views import ProductListQuerysetMixin
from .serializers import ProductSerializer


class ProductViewSet(ProductListQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = ProductSerializer
    search_fields = ['name', 'price']
    # pagination_class = None
    # page_size = 1000

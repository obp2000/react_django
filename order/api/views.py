"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet

from ..models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.details()
    serializer_class = OrderSerializer
    search_fields = ['customer__nick', 'customer__name']

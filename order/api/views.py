"""
API endpoints that allow models to be viewed or edited.
"""
from react_django.api.consts import get_options
from rest_framework.viewsets import ModelViewSet

from ..models import Order
from .consts_data import consts_data
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.details()
    serializer_class = OrderSerializer
    search_fields = ['customer__nick', 'customer__name']

    def options(self, request, *args, **kwargs):
        return get_options(self, request, consts_data)

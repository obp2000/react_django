"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from ..models import DeliveryType
from ..views import OrderListQuerysetMixin
from .serializers import DeliveryTypeSerializer, OrderSerializer


class DeliveryTypeList(ListAPIView):
    """
    API endpoint that allows delivery types to be listed.
    """
    # queryset = DeliveryType.local
    queryset = DeliveryType
    serializer_class = DeliveryTypeSerializer
    pagination_class = None


class OrderViewSet(OrderListQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    # queryset = Order.orders.list()
    serializer_class = OrderSerializer

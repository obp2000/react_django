"""
API endpoints that allow models to be viewed.
"""
from rest_framework.generics import ListAPIView
from .models import DeliveryType
from .serializers import DeliveryTypeSerializer


class DeliveryTypeList(ListAPIView):
    """
    API endpoint that allows delivery types to be listed.
    """
    # queryset = DeliveryType.local
    queryset = DeliveryType
    serializer_class = DeliveryTypeSerializer
    pagination_class = None

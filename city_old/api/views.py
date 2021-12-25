"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet

from ..models import City
from .serializers import CitySerializer


class CityViewSet(ModelViewSet):
    """
    API endpoint that allows cities to be viewed and searched.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None
    search_fields = ['pindex', 'city']

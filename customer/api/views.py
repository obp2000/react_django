"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet

from ..models import City
from ..views import CustomerQuerysetMixin
from .serializers import CitySerializer, CustomerSerializer


class CityViewSet(ModelViewSet):
    """
    API endpoint that allows cities to be viewed and searched.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # pagination_class = None
    search_fields = ['pindex', 'city']


class CustomerViewSet(CustomerQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    serializer_class = CustomerSerializer
    search_fields = ['nick', 'name', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]

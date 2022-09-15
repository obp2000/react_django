"""
API endpoints that allow models to be viewed or edited.
"""
from react_django.api.consts import get_options
from rest_framework.viewsets import ModelViewSet

from ..models import City
from ..views import CustomerQuerysetMixin
from .consts_data import consts_data
from .serializers import CitySerializer, CustomerSerializer


class CityViewSet(ModelViewSet):
    """
    API endpoint that allows cities to be viewed and searched.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # pagination_class = None
    search_fields = ['^city', '^pindex']



class CustomerViewSet(CustomerQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    serializer_class = CustomerSerializer
    search_fields = ['nick', 'name', 'city__city', 'city__pindex', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]

    def options(self, request, *args, **kwargs):
        return get_options(self, request, consts_data)

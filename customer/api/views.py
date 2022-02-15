"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import City, Customer
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
    search_fields = ['nick', 'name', 'city__city', 'city__pindex', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        data['name'] = Customer._meta.verbose_name.capitalize()
        return Response(data=data, status=status.HTTP_200_OK)

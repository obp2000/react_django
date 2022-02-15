"""
API endpoints that allow models to be viewed or edited.
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import Product, ProductType
from ..views import ProductQuerysetMixin
from .serializers import ProductSerializer, ProductTypeSerializer


class ProductTypeViewSet(ModelViewSet):
    """
    API endpoint that allows product types to be viewed and searched.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    search_fields = ['name']


class ProductViewSet(ProductQuerysetMixin, ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = ProductSerializer
    search_fields = ['name', 'product_type__name', 'price']
    # pagination_class = None
    # page_size = 1000

    def options(self, request, *args, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        data['name'] = Product._meta.verbose_name.capitalize()
        if data.get('actions', None):
            for method in ['PUT', 'POST']:
                if data['actions'].get(method, None):
                    data['actions'][method]['product_type'] = {}
                    data['actions'][method]['product_type']['label'] = \
                        ProductType._meta.verbose_name.capitalize()
                    data['actions'][method]['new_image'] = {}
                    data['actions'][method]['new_image']['label'] = \
                        Product._meta.get_field('image').verbose_name.capitalize()
                    data['actions'][method]['product_type']['choices'] = \
                        ProductTypeSerializer.options()
                    data['actions'][method]['prices'] = {}
                    data['actions'][method]['prices']['label'] = \
                        _('meter price').capitalize()
                    data['actions'][method]['density_for_count'] = {}
                    data['actions'][method]['density_for_count']['label'] = \
                        _('density for count').capitalize()
                    data['actions'][method]['meters_in_roll'] = {}
                    data['actions'][method]['meters_in_roll']['label'] = \
                        _('meters in roll').capitalize()
        return Response(data=data, status=status.HTTP_200_OK)

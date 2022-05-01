"""
API Serializers.
"""
from collections import ChainMap

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from ..models import Product, ProductType


class ProductTypeSerializer(ModelSerializer):
    """
    City serializer.
    """
    class Meta:
        """
        Set City serializer.
        """
        model = ProductType
        fields = ['id', 'name']

    @classmethod
    def options(cls):
        return cls(ProductType.options, many=True).data


class ProductSerializer(ModelSerializer):
    """
    Product serializer.
    """
    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        fields = ['id', 'name',
                  'product_type', 'get_product_type_display',
                  'threads', 'get_threads_display',
                  'contents', 'get_contents_display',
                  'fleece', 'price',
                  'weight', 'width', 'density', 'dollar_price', 'dollar_rate',
                  'width_shop', 'density_shop', 'weight_for_count',
                  'length_for_count', 'price_pre', 'image', 'created_at',
                  'updated_at']

    select_fields = ['product_type', 'threads', 'contents']

    values_map = {'true': True,
                  'false': False,
                  '': None}

    def to_internal_value(self, data):
        # print('product_data: ', data)
        data_dict = data.dict()
        print('product_data: ', data_dict)
        mapped_fields = {key: self.values_map[value] for
                         key, value in data_dict.items() if
                         value in self.values_map}
        blank_fields = {select_field: None for
                        select_field in self.select_fields}
        return ChainMap(mapped_fields, data_dict, blank_fields)

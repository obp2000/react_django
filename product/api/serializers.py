"""
API Serializers.
"""
from react_django.api.serializers import WritableNestedModelSerializer
from rest_framework.serializers import (ChoiceField, ModelSerializer,
                                        SerializerMethodField)

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


class ProductSerializer(ModelSerializer):
    """
    Product serializer.
    """
    product_type = ProductTypeSerializer()
    product_type_options = SerializerMethodField()

    def get_product_type_options(self, product):
        return ([ProductTypeSerializer({'id': None, 'name': '----'}).data] +
                [ProductTypeSerializer(product_type).data for product_type
                 in ProductType.objects.all()])

    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        fields = ['id', 'name', 'product_type', 'product_type_options',
                  'threads', 'get_threads_display',
                  'contents', 'get_contents_display',
                  'fleece', 'price',
                  'weight', 'width', 'density', 'dollar_price', 'dollar_rate',
                  'width_shop', 'density_shop', 'weight_for_count',
                  'length_for_count', 'price_pre', 'image', 'created_at',
                  'updated_at']

    remove_keys = ['product_type[id]', 'product_type[name]',
                   'contents[value]', 'contents[display_name]',
                   'threads[value]', 'threads[display_name]']

    def to_internal_value(self, data):
        data_dict = data.dict()
        print('data: ', data_dict)
        if data_dict.get('product_type[id]', None):
            data_dict['product_type'] = {}
            data_dict['product_type']['id'] = data_dict['product_type[id]']
            data_dict['product_type']['name'] = data_dict['product_type[name]']
            data_dict['product_type'] = ProductType(
                **data_dict['product_type'])
        elif data_dict.get('product_type[id]', None) == '':
            # data_dict['product_type'] = {}
            data_dict['product_type'] = None
        if data_dict.get('contents[value]', None):
            data_dict['contents'] = data_dict['contents[value]']
        elif data_dict.get('contents[value]', None) == '':
            data_dict['contents'] = None
        if data_dict.get('threads[value]', None):
            data_dict['threads'] = data_dict['threads[value]']
        elif data_dict.get('threads[value]', None) == '':
            data_dict['threads'] = None
        if data_dict.get('fleece', None) == 'true':
            data_dict['fleece'] = True
        elif data_dict.get('fleece', None) == 'false':
            data_dict['fleece'] = False

        for key in self.remove_keys:
            data_dict.pop(key, None)
        for key, value in data_dict.items():
            if value == '':
                data_dict[key] = None
        return data_dict


class ProductSelectSerializer(ModelSerializer):
    """
    Product serializer for select field.
    """
    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        fields = ['id', 'name', 'price', 'weight', 'width',
                  'density', 'threads']

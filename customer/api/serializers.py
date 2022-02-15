"""
API Serializers.
"""
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.serializers import ModelSerializer

from ..models import City, Customer


class CitySerializer(ModelSerializer):
    """
    City serializer.
    """
    class Meta:
        """
        Set City serializer.
        """
        model = City
        fields = ['id', 'pindex', 'city']
        # fields ='__all__'


class CustomerSerializer(ModelSerializer):
    """
    Customer serializer.
    """
    city = CitySerializer()

    class Meta:
        """
        Set Customer serializer.
        """
        model = Customer
        fields = ['id', 'nick', 'name', 'city', 'address',
                  'created_at', 'updated_at']

    def to_internal_value(self, data):
        print('customer_data: ', data)
        return data

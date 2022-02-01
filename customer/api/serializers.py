"""
API Serializers.
"""
from react_django.api.serializers import WritableNestedModelSerializer
from rest_framework.serializers import (CharField, ModelSerializer,
                                        ReadOnlyField, ValidationError)

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
        # read_only_fields = ['id','pindex', 'city']


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
        print('data: ', data)
        if data.get('city', None) and data['city'].get('id', None):
            data['city'] = City(**data['city'])
        else:
            data.pop('city', None)
        return data

    # def validate1(self, data):
    #     print('validate: ', data)
    #     if data.get('city', None) and data['city'].get('id', None):
    #         data['city'] = City(**data['city'])
    #     else:
    #         data.pop('city', None)
    #     return super().validate(data)



class CustomerSelectSerializer(WritableNestedModelSerializer):
    """
    Customer serializer for select field.
    """
    city = CitySerializer()

    class Meta:
        """
        Set Customer serializer.
        """
        model = Customer
        fields = ['id', 'nick', 'name', 'city', 'address']

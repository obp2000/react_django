"""
API Serializers.
"""
from react_django.utils import WritableNestedModelSerializerMod
from rest_framework.serializers import ModelSerializer
from city.serializers import CitySerializer
from .models import Customer


class CustomerSerializer(WritableNestedModelSerializerMod):
    """
    Customer serializer.
    """
    city = CitySerializer()

    class Meta:
        """
        Set Customer serializer.
        """
        model = Customer
        fields = '__all__'


class CustomerSelectSerializer(ModelSerializer):
    """
    Customer serializer for select field.
    """
    city = CitySerializer()
    
    class Meta:
        """
        Set Customer serializer.
        """
        model = Customer
        fields = ['id', 'nick', 'name', 'city']
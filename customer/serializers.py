"""
API Serializers.
"""
from react_django.utils import WritableNestedModelSerializerMod
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

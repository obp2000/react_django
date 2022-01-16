"""
API Serializers.
"""
from react_django.api.serializers import WritableNestedModelSerializerMod
from rest_framework.serializers import CharField, ModelSerializer

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
        fields = '__all__'


class CustomerSerializer(WritableNestedModelSerializerMod):
    """
    Customer serializer.
    """
    city = CitySerializer()
    pindex = CharField(read_only=True)

    class Meta:
        """
        Set Customer serializer.
        """
        model = Customer
        fields = '__all__'

    def validate(self, attrs):
        attrs.pop('pindex', None)
        return super().validate(attrs)


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

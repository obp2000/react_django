"""
API Serializers.
"""
from rest_framework.serializers import ModelSerializer

from ..models import City


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

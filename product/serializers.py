"""
API Serializers.
"""
from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    """
    Product serializer.
    """
    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        fields = '__all__'


class ProductSelectSerializer(ModelSerializer):
    """
    Product serializer for select field.
    """
    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        fields = ['id', 'name', 'price', 'weight', 'width', 'density']

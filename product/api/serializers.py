"""
API Serializers.
"""
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..models import Product


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
    # one_m_weight = SerializerMethodField()
    class Meta:
        """
        Set Product serializer.
        """
        model = Product
        # queryset = Product.objects.details
        fields = ['id', 'name', 'price', 'weight', 'width', 'density']

    # def get_one_m_weight(self, obj):
    #     return obj.one_m_weight

"""
API Serializers.
"""
from react_django.utils import WritableNestedModelSerializerMod
from product.serializers import ProductSelectSerializer
from .models import OrderItem


class OrderItemSerializer(WritableNestedModelSerializerMod):
    """
    Order item serializer.
    """
    product = ProductSelectSerializer()

    class Meta:
        """
        Set Order item serializer.
        """
        model = OrderItem
        fields = '__all__'

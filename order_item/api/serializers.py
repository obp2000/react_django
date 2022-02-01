"""
API Serializers.
"""
from product.api.serializers import ProductSelectSerializer
# from product.models import Product
from react_django.api.serializers import WritableNestedModelSerializerMod
from rest_framework.serializers import (DecimalField, IntegerField,
                                        ReadOnlyField, SerializerMethodField)

from ..models import OrderItem


class OrderItemSerializer(WritableNestedModelSerializerMod):
    """
    Order item serializer.
    """
    product = ProductSelectSerializer()
    # cost = ReadOnlyField()
    # weight = ReadOnlyField()

    class Meta:
        """
        Set Order item serializer.
        """
        model = OrderItem
        # fields = ['id', 'order', 'product', 'amount', 'price', 'cost',
        #     'weight']
        fields = '__all__'

    # def validate(self, attrs):
    #     attrs.pop('cost', None)
    #     attrs.pop('weight', None)
    #     return super().validate(attrs)

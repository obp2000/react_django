"""
API Serializers.
"""
# from drf_writable_nested.serializers import WritableNestedModelSerializer
from product.api.serializers import ProductSerializer
# from product.models import Product
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from ..forms import OrderItemForm
from ..models import OrderItem


class OrderItemSerializer(ModelSerializer):
    """
    Order item serializer.
    """
    product = ProductSerializer(
        label=OrderItem._meta.get_field('product').verbose_name.capitalize())
    cost = ReadOnlyField(label=OrderItemForm().fields['cost'].label)
    weight = ReadOnlyField(label=OrderItemForm().fields['weight'].label)

    class Meta:
        """
        Set Order item serializer.
        """
        model = OrderItem
        fields = ['id', 'order', 'product', 'amount', 'price', 'cost', 'weight']

    def to_internal_value(self, data):
        print('order_item_data: ', data)
        return data

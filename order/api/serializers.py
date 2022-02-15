"""
API Serializers.
"""
from collections import ChainMap

from customer.api.serializers import CustomerSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from order_item.api.serializers import OrderItemSerializer
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from ..models import DeliveryType, Order, Packet


class OrderSerializer(WritableNestedModelSerializer):
    """
    Order serializer.
    """
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(many=True, allow_null=True)
    order_items_amount = ReadOnlyField()
    order_items_cost = ReadOnlyField()
    order_items_weight = ReadOnlyField()

    select_fields = ['delivery_type','packet']

    def to_internal_value(self, data):
        print('order_data: ', data)
        return ChainMap(data, {select_field: None for
            select_field in self.select_fields})

    class Meta:
        """
        Set Order detail serializer.
        """
        model = Order
        fields = ['id', 'customer', 'post_cost', 'packet', 'delivery_type',
            'address', 'gift', 'order_items', 'order_items_amount',
            'order_items_cost', 'order_items_weight', 'created_at', 'updated_at']

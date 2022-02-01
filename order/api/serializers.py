"""
API Serializers.
"""
from customer.api.serializers import CustomerSelectSerializer
from order_item.api.serializers import OrderItemSerializer
from react_django.api.serializers import WritableNestedModelSerializer
from rest_framework.serializers import (BaseSerializer, CharField, ChoiceField,
                                        DateTimeField, DecimalField,
                                        HiddenField, IntegerField,
                                        ModelSerializer,
                                        PrimaryKeyRelatedField, ReadOnlyField,
                                        Serializer, SerializerMethodField)

from ..models import DeliveryType, Order, Packet


class OrderSerializer(WritableNestedModelSerializer):
    """
    Order serializer.
    """
    customer = CustomerSelectSerializer()
    order_items = OrderItemSerializer(many=True, allow_null=True)
    order_items_cost = ReadOnlyField()
    order_items_weight = ReadOnlyField()
    # created_at = ReadOnlyField()

    def validate(self, attrs):
        if type(attrs.get('delivery_type', None)) == dict:
            attrs['delivery_type'] = attrs['delivery_type']['value']
        if type(attrs.get('packet', None)) == dict:
            attrs['packet'] = attrs['packet']['value']
        return super().validate(attrs)

    class Meta:
        """
        Set Order detail serializer.
        """
        model = Order
        # fields = '__all__'
        fields = ['id', 'customer', 'post_cost', 'packet', 'delivery_type',
            'address', 'gift', 'order_items', 'order_items_cost',
            'order_items_weight', 'created_at', 'updated_at']

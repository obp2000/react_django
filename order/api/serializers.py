"""
API Serializers.
"""
from customer.api.serializers import CustomerSerializer
from order_item.api.serializers import OrderItemSerializer
from react_django.api.serializers import WritableNestedModelSerializerMod
from rest_framework.serializers import (BaseSerializer, CharField,
                                        IntegerField, ModelSerializer,
                                        Serializer)

from ..models import DeliveryType, Order

# from delivery_type.models import DeliveryType


class DeliveryTypeSerializer2(ModelSerializer):
    """
    Delivery type serializer.
    """
    class Meta:
        """
        Set Delivery type serializer.
        """
        model = DeliveryType
        fields = '__all__'


class DeliveryTypeSerializer(Serializer):
    """
    Delivery type serializer.
    """
    value = IntegerField()
    label = CharField()

    # def to_representation(self, instance):
    #     return instance


class OrderSerializer(WritableNestedModelSerializerMod):
    """
    Order serializer.
    """
    sum = IntegerField(read_only=True)
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(many=True, allow_null=True)

    def validate(self, attrs):
        if attrs["delivery_type"] == "":
            attrs["delivery_type"] = None
        return super().validate(attrs)

    class Meta:
        """
        Set Order detail serializer.
        """
        model = Order
        fields = '__all__'

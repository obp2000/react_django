"""
API Serializers.
"""
from rest_framework.serializers import IntegerField
from react_django.utils import WritableNestedModelSerializerMod
from customer.serializers import CustomerSerializer
from order_item.serializers import OrderItemSerializer
from .models import Order
# from delivery_type.models import DeliveryType


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

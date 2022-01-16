"""
API Serializers.
"""
from customer.api.serializers import CustomerSerializer
from django.utils.timezone import now
from order_item.api.serializers import OrderItemSerializer
from react_django.api.serializers import WritableNestedModelSerializerMod
from rest_framework.serializers import (BaseSerializer, CharField,
                                        DateTimeField, HiddenField,
                                        IntegerField, ModelSerializer,
                                        ReadOnlyField, Serializer,
                                        SerializerMethodField)

from ..models import DeliveryType, Order

# from delivery_type.models import DeliveryType

# class DeliveryTypeSerializer(Serializer):
#     """
#     Delivery type serializer.
#     """
#     id = IntegerField()
#     label = CharField()

#     # def to_representation(self, instance):
#     #     # return {'value': instance[0],
#     #     #         'label': instance[1]}
#     #     return instance
#     def to_internal_value(self, data):
#         return data.get('id', None)


class OrderSerializer(WritableNestedModelSerializerMod):
    """
    Order serializer.
    """
    sum = IntegerField(read_only=True)
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(many=True, allow_null=True)
    # delivery_types = DeliveryTypeSerializer(many=True, allow_null=True, read_only=True)
    delivery_types = SerializerMethodField()
    created_at = DateTimeField(read_only=True)

    def validate(self, attrs):
        # attrs.pop('created_at', None)
        if type(attrs.get('delivery_type', None)) == dict:
            attrs['delivery_type'] = attrs['delivery_type']['id']
        return super().validate(attrs)

    class Meta:
        """
        Set Order detail serializer.
        """
        model = Order
        fields = '__all__'
        # read_only_fields = ['created_at']

    def get_delivery_types(self, obj):
        return [{'id': delivery_type[0],
                 'label': delivery_type[1]} for delivery_type in DeliveryType.choices]

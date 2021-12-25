"""
API Serializers.
"""
from rest_framework.serializers import (BaseSerializer, CharField,
                                        IntegerField, ModelSerializer,
                                        Serializer)

from .models import DeliveryType


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

"""
API Serializers.
"""
# from rest_framework.serializers import (ModelSerializer,
#                                         BaseSerializer,
#                                         IntegerField,
#                                         CharField,
#                                         Serializer)
# from drf_writable_nested.serializers import WritableNestedModelSerializer
# # from django.core.files.uploadedfile import InMemoryUploadedFile
# from .models import Order

# from customer.serializers import CustomerSerializer
# from order_item.serializers import OrderItemSerializer
# from product.serializers import ProductSelectSerializer


# class CitySerializer(ModelSerializer):
#     """
#     City serializer.
#     """
#     class Meta:
#         """
#         Set City serializer.
#         """
#         model = City
#         fields = '__all__'


# class WritableNestedModelSerializerMod(WritableNestedModelSerializer):
    
#     Writable Nested Model Serializer modified.
    
#     def to_internal_value(self, data):
#         data.pop('created_at', None)
#         data.pop('_destroy', None)
#         return data


# class CustomerSerializer(WritableNestedModelSerializerMod):
#     """
#     Customer serializer.
#     """
#     city = CitySerializer()

#     class Meta:
#         """
#         Set Customer serializer.
#         """
#         model = Customer
#         fields = '__all__'


# class ProductSerializer(ModelSerializer):
#     """
#     Product serializer.
#     """
#     class Meta:
#         """
#         Set Product serializer.
#         """
#         model = Product
#         fields = '__all__'


# class ProductSelectSerializer(ModelSerializer):
#     """
#     Product serializer for select field.
#     """
#     class Meta:
#         """
#         Set Product serializer.
#         """
#         model = Product
#         fields = ['id', 'name', 'price', 'weight', 'width', 'density']


# class OrderItemSerializer(WritableNestedModelSerializerMod):
#     """
#     Order item serializer.
#     """
#     product = ProductSelectSerializer()

#     class Meta:
#         """
#         Set Order item serializer.
#         """
#         model = OrderItem
#         fields = '__all__'


# class OrderSerializer(WritableNestedModelSerializerMod):
#     """
#     Order serializer.
#     """
#     sum = IntegerField(read_only=True)
#     customer = CustomerSerializer()
#     order_items = OrderItemSerializer(many=True, allow_null=True)

#     class Meta:
#         """
#         Set Order detail serializer.
#         """
#         model = Order
#         fields = '__all__'


# class DeliveryTypeSerializer(BaseSerializer):
#     """
#     Delivery type serializer.
#     """
#     def to_representation(self, instance):
#         return instance


# class DeliveryTypeSerializer2(Serializer):
#     """
#     Delivery type serializer.
#     """
#     local = CharField()

# class ProductWriteSerializer(ModelSerializer):
#     """
#     Product serializer.
#     """
#     class Meta:
#         """
#         Set Product serializer.
#         """
#         model = Product
#         fields = (
#             'id',
#             'name',
#             'price',
#             'weight',
#             'width',
#             'density',
#             'dollar_price',
#             'dollar_rate',
#             'width_shop',
#             'density_shop',
#             'weight_for_count',
#             'length_for_count',
#             'price_pre',
#             'image',
#         )

#     def to_internal_value(self, data):
#         result = {}
#         keys = data.keys() - ['created_at', 'updated_at', 'image']
#         for key in keys:
#             result[key] = data.get(key, None) or None
#         image = data.get('image', None)
#         if type(image) == InMemoryUploadedFile:
#             result['image'] = image
#         return result

# class OrderWriteSerializer(WritableNestedModelSerializer):
#     """
#     Order write serializer.
#     """
#     customer = CustomerSerializer()
#     order_items = OrderItemSerializer(many=True, allow_null=True)

#     class Meta:
#         """
#         Set Order detail serializer.
#         """
#         model = Order
#         fields = '__all__'
#         # fields = (
#         #     'id',
#         #     'post_cost',
#         #     'packet',
#         #     'delivery_type',
#         #     'address',
#         #     'gift',
#         #     'customer',
#         #     'order_items',
#         # )

#     def to_internal_value(self, data):
#         data.pop('created_at', None)
#         data.pop('updated_at', None)
#         customer = data.get('customer', None)
#         data['customer']['id'] = customer['id'] if type(customer) == dict else None
#         return data

#     # def update1(self, instance, validated_data):
#     #     # order_items_data = validated_data.pop('order_items')
#     #     order_items = (instance.order_items).all()
#     #     order_items = list(order_items)
#     #     instance.post_cost = validated_data.get(
#     #         'post_cost', instance.post_cost)
#     #     instance.packet = validated_data.get('packet', instance.packet)
#     #     instance.delivery_type = validated_data.get(
#     #         'delivery_type', instance.delivery_type)
#     #     instance.address = validated_data.get('address', instance.address)
#     #     instance.gift = validated_data.get('gift', instance.gift)
#     #     instance.customer = validated_data.get('customer', instance.customer)
#     #     instance.save()
#     #     print(json.dumps(validated_data))

#     #     for order_item_data in order_items_data:
#     #         order_item = order_items.pop(0)
#     #         order_item.amount = order_item_data.get('amount', order_item.amount)
#     #         order_item.price = order_item_data.get('price', order_item.price)
#     #         order_item.product = order_item_data.get('product', order_item.product)
#     #         order_item.order = order_item_data.get('order', order_item.order)
#     #         order_item.save()
#     #     return instance


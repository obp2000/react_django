from drf_writable_nested.serializers import WritableNestedModelSerializer


class WritableNestedModelSerializerMod(WritableNestedModelSerializer):
    """
    Writable Nested Model Serializer modified.
    """
    def to_internal_value1(self, data):
        # data.pop('created_at', None)
        # data.pop('_destroy', None)
        # data.pop('pindex', None)
        # if type(data.get('delivery_type', None)) == dict:
        #     data['delivery_type'] = data['delivery_type']['id']
        return data

    # def validate(self, attrs):
    #     print(attrs)
    #     if type(attrs.get('city', None)) == dict:
    #         # attrs['delivery_type'] = attrs['delivery_type']['id']
    #         # attrs1 = attrs.clone()
    #         attrs1.pop['city']
    #     return super().validate(attrs1)

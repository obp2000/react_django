from drf_writable_nested.serializers import WritableNestedModelSerializer


class WritableNestedModelSerializerMod(WritableNestedModelSerializer):
    """
    Writable Nested Model Serializer modified.
    """

    def to_internal_value(self, data):
        data.pop('created_at', None)
        data.pop('_destroy', None)
        # if type(data.get('delivery_type', None)) == dict:
        #     data['delivery_type'] = data['delivery_type']['id']
        return data

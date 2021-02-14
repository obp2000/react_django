from rest_framework import pagination
from rest_framework.response import Response

from django.test.runner import DiscoverRunner

from drf_writable_nested.serializers import WritableNestedModelSerializer


class PageNumberPaginationWithNumPages(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'totalCount': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'results': data
        })


class UnManagedModelTestRunner(DiscoverRunner):

    def setup_test_environment(self, *args, **kwargs):
        from django.apps import apps
        get_models = apps.get_models
        self.unmanaged_models = [
            m for m in get_models() if not m._meta.managed]
        for m in self.unmanaged_models:
            m._meta.managed = True
        super().setup_test_environment(*args, **kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        super().teardown_test_environment(*args, **kwargs)
        for m in self.unmanaged_models:
            m._meta.managed = False


class WritableNestedModelSerializerMod(WritableNestedModelSerializer):
    """
    Writable Nested Model Serializer modified.
    """

    def to_internal_value(self, data):
        data.pop('created_at', None)
        data.pop('_destroy', None)
        return data

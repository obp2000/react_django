from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPaginationWithNumPages(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'totalCount': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'results': data
        })

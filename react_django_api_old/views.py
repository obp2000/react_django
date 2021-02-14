# """
# API endpoints that allow models to be viewed or edited.
# """

# # from django.db.models import Sum, F
# from rest_framework.viewsets import ModelViewSet
# # from rest_framework.mixins import ListModelMixin
# # from rest_framework import permissions
# from .models import Order
# from .serializers import OrderSerializer


# class CityViewSet(ModelViewSet):
#     """
#     API endpoint that allows cities to be viewed and searched.
#     """
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#     pagination_class = None
#     search_fields = ['pindex', 'city']


# class CustomerViewSet(ModelViewSet):
#     """
#     API endpoint that allows customers to be viewed or edited.
#     """
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     search_fields = ['nick', 'name', 'address']
#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]


# class ProductViewSet(ModelViewSet):
#     """
#     API endpoint that allows products to be viewed or edited.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     search_fields = ['name', 'price']
#     # pagination_class = None
#     # page_size = 1000


# class OrderViewSet(ModelViewSet):
#     """
#     API endpoint that allows orders to be viewed or edited.
#     """
#     # queryset = Order.objects.annotate(sum=Sum(F('order_items__price')
#     #                                           * F('order_items__amount')))
#     queryset = Order.orders.all_with_sum()
#     serializer_class = OrderSerializer


# class DeliveryTypeList(GenericViewSet, ListModelMixin):
    
#     API endpoint that allows delivery types to be viewed and searched.
    
#     queryset = DeliveryType.local
#     serializer_class = DeliveryTypeSerializer
#     pagination_class = None

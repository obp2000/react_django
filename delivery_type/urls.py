from django.urls import path
from .views import DeliveryTypeList

urlpatterns = [
    path('delivery_types/', DeliveryTypeList.as_view(),
         name='delivery_type-list')
]

from django.urls import path
from .views import (OrderList, OrderCreate,
                    OrderUpdate, OrderDelete)

urlpatterns = [
    path('new/', OrderCreate.as_view(), name='order-new'),
    path('<int:pk>/', OrderUpdate.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order-delete'),
    path('', OrderList.as_view(), name='order-list')
]

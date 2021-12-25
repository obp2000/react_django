from django.urls import path

from .views import OrderCreate, OrderDelete, OrderList, OrderUpdate

urlpatterns = [
    path('new/', OrderCreate.as_view(), name='order-new'),
    path('<int:pk>/', OrderUpdate.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order-delete'),
    path('', OrderList.as_view(), name='order-list')
]

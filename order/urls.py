from django.urls import path

from .views import OrderCreate, OrderDelete, OrderList, OrderUpdate

app_name = 'order'

urlpatterns = [
    path('new/', OrderCreate.as_view(), name='new'),
    path('<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='delete'),
    path('', OrderList.as_view(), name='list')
]

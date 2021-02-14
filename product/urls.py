from django.urls import path
from .views import (ProductList, ProductCreate,
                    ProductUpdate, ProductDelete)

urlpatterns = [
    path('new/', ProductCreate.as_view(), name='product-new'),
    path('<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('', ProductList.as_view(), name='product-list')
]

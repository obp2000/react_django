from django.urls import path

from .views import ProductCreate, ProductDelete, ProductList, ProductUpdate

urlpatterns = [
    path('new/', ProductCreate.as_view(), name='product-new'),
    path('<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('', ProductList.as_view(), name='product-list')
]

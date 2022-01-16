from django.urls import path

from .views import ProductCreate, ProductDelete, ProductList, ProductUpdate

app_name = 'product'

urlpatterns = [
    path('new/', ProductCreate.as_view(), name='new'),
    path('<int:pk>/', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    path('', ProductList.as_view(), name='list')
]

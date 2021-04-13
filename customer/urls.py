from django.urls import path
from .views import CustomerList, CustomerCreate, CustomerUpdate, CustomerDelete

urlpatterns = [
    path('new/', CustomerCreate.as_view(), name='customer-new'),
    path('<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('<int:pk>/delete/', CustomerDelete.as_view(), name='customer-delete'),
    path('', CustomerList.as_view(), name='customer-list'),
]

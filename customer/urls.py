from django.urls import path

from .views import CustomerCreate, CustomerDelete, CustomerList, CustomerUpdate

app_name = 'customer'

urlpatterns = [
    path('new/', CustomerCreate.as_view(), name='new'),
    path('<int:pk>/', CustomerUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CustomerDelete.as_view(), name='delete'),
    path('', CustomerList.as_view(), name='list'),
]

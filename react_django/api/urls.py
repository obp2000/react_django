from customer.api.views import CityViewSet, CustomerViewSet
from django.urls import include, path
from order.api.views import OrderViewSet
from product.api.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
# router.register(r'delivery_types', DeliveryTypeViewSet,
#                 basename='delivery_type')

urlpatterns = [
    path('', include((router.urls, 'api',))),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
]

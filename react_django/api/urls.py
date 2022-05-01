from customer.api.views import CityViewSet, CustomerViewSet
from django.urls import include, path
from order.api.views import OrderViewSet
from product.api.views import ProductTypeViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from user_auth.api.views import UserDetailsView

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_types', ProductTypeViewSet)
router.register(r'orders', OrderViewSet)
router.register('', CustomerViewSet)

urlpatterns = [
    path('user/', UserDetailsView.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('', include((router.urls, 'api',)))
]

"""react_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from ajax_select import urls as ajax_select_urls
import debug_toolbar
# from customer.api.views import CityViewSet, CustomerViewSet
from customer.views import CustomerList
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from .api.urls import api_urls

# from order.api.views import DeliveryTypeViewSet, OrderViewSet
# from product.api.views import ProductViewSet
# from rest_framework.routers import DefaultRouter

# from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view

# router = DefaultRouter()
# router.register(r'cities', CityViewSet)
# router.register(r'customers', CustomerViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'orders', OrderViewSet)
# router.register(r'delivery_types', DeliveryTypeViewSet,
#                 basename='delivery_type')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include("react_django.select2")),
    path('api/', include('react_django.api.urls')),
    # path('api/', include('dj_rest_auth.urls')),
    # path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('customers/', include('customer.urls', namespace='customer')),
    path('products/', include('product.urls', namespace='product')),
    path('orders/', include('order.urls', namespace='order')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('user_auth.urls')),
    path('', CustomerList.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

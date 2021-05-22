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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from ajax_select import urls as ajax_select_urls
import debug_toolbar
from rest_framework.routers import DefaultRouter
from city.views import CityViewSet
from customer.views import CustomerList, CustomerViewSet
from product.views import ProductViewSet
from order.views import OrderViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('api/', include('delivery_type.urls')),
    # path('ajax_select/', include(ajax_select_urls)),
    path("select2/", include("react_django.select2")),
    path('auth/', include('user_auth.token_urls')),
    path('', include('user_auth.urls')),
    path('admin/', admin.site.urls),
    path('customers/', include('customer.urls', namespace='customer')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', CustomerList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

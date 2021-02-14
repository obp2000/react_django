"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'price']
    # pagination_class = None
    # page_size = 1000


class ProductList(ListView):
    model = Product
    paginate_by = 10


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    # fields = '__all__'
    # success_url = reverse_lazy('items:index')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = '__all__'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

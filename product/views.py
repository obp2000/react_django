"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.urls import reverse_lazy
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Product
from .forms import ProductForm, ProductFilterFormHelper, DeleteProductForm
from .serializers import ProductSerializer
from .tables import ProductTable
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'price']
    # pagination_class = None
    # page_size = 1000


class ProductList(SingleTableMixin, FilterView):
    # model = Product
    table_class = ProductTable
    table_pagination = {'per_page': 5}
    template_name_suffix = '_list'
    filterset_class = ProductFilter
    extra_context = {'product_filter_helper': ProductFilterFormHelper,
                     'delete_product_form': DeleteProductForm}


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')
    success_message = _("%(name)s was created successfully")


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_message = _("%(name)s was updated successfully")


class ProductDelete(BSModalDeleteView):
    model = Product
    extra_context = {'form': DeleteProductForm}
    success_url = reverse_lazy('product-list')
    success_message = _("%(name)s was deleted successfully")
"""
API endpoints that allow models to be viewed or edited.
"""

from rest_framework.viewsets import ModelViewSet
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from bootstrap_modal_forms.generic import BSModalDeleteView
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from react_django.forms import DeleteFormHelper, DeleteObjectForm, \
    FilterFormHelper
from .models import Product
from .forms import ProductForm, ProductFormHelper
from .serializers import ProductSerializer
from .tables import ProductTable
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.products.select_related("product_type").all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'price']
    # pagination_class = None
    # page_size = 1000


class ProductList(SingleTableMixin, FilterView):
    queryset = Product.products.select_related("product_type").all()
    table_class = ProductTable
    table_pagination = {'per_page': 5}
    filterset_class = ProductFilter
    template_name = "object_list.html"
    extra_context = {'filter_helper': FilterFormHelper(
        filter_fields=ProductFilter._meta.fields),
                     'delete_object_form': DeleteObjectForm,
                     'delete_path_name': 'product-delete',
                     'table_title': _("products").capitalize(),
                     'new_url': reverse_lazy('product-new'),
                     'list_url': reverse_lazy('product-list')}


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    queryset = Product.products.details()
    form_class = ProductForm
    template_name = "object_form.html"
    success_url = reverse_lazy('product-list')
    success_message = _("%(name)s was created successfully")
    extra_context = {'object_form_helper': ProductFormHelper}


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    queryset = Product.products.details()
    form_class = ProductForm
    template_name = "object_form.html"
    success_message = _("%(name)s was updated successfully")
    extra_context = {'object_form_helper': ProductFormHelper}

    def get_initial(self):
        return {
            'price_rub_m': self.object.price_rub_m,
            'density_for_count': self.object.density_for_count,
            'meters_in_roll': '{:.2f}'.format(self.object.meters_in_roll) if \
                                    self.object.meters_in_roll else None
            }


class ProductDelete(BSModalDeleteView):
    model = Product
    extra_context = {'form': DeleteObjectForm,
                     'delete_form_helper': DeleteFormHelper}
    template_name = "object_confirm_delete.html"
    success_url = reverse_lazy('product-list')
    success_message = "%s %s" % (_("product").capitalize(), _("was deleted successfully"))

"""
API endpoints that allow models to be viewed or edited.
"""

from bootstrap_modal_forms.generic import BSModalDeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from react_django.forms import (DeleteFormHelper, DeleteObjectForm,
                                FilterFormHelper)

from .filters import ProductFilter
from .forms import ProductForm, ProductFormHelper
from .models import Product
from .tables import ProductTable


class ProductListQuerysetMixin:
    queryset = Product.objects.select_related("product_type")


class ProductSuccessUrlMixin:
    success_url = reverse_lazy('product:list')


class ProductEditMixin(ProductSuccessUrlMixin):
    queryset = Product.objects.details()
    form_class = ProductForm
    template_name = "object_form.html"
    extra_context = {'object_form_helper': ProductFormHelper}


class ProductList(ProductListQuerysetMixin, SingleTableMixin, FilterView):
    table_class = ProductTable
    table_pagination = {'per_page': 5}
    filterset_class = ProductFilter
    template_name = "object_list.html"
    extra_context = {
        'filter_helper':
        FilterFormHelper(filter_fields=ProductFilter._meta.fields),
        'delete_object_form': DeleteObjectForm,
        'delete_path_name': 'product:delete',
        'table_title': _("products").capitalize(),
        'new_url': reverse_lazy('product:new'),
        'list_url': reverse_lazy('product:list')
    }


class ProductCreate(ProductEditMixin, SuccessMessageMixin, CreateView):
    success_message = _("%(name)s was created successfully")


class ProductUpdate(ProductEditMixin, SuccessMessageMixin, UpdateView):
    success_message = _("%(name)s was updated successfully")

    def get_initial(self):
        return {
            'price_rub_m':
            self.object.price_rub_m,
            'density_for_count':
            self.object.density_for_count,
            'meters_in_roll':
            f'{self.object.meters_in_roll:.2f}'
            if self.object.meters_in_roll else None
        }


class ProductDelete(ProductSuccessUrlMixin, ProductListQuerysetMixin,
                    BSModalDeleteView):
    extra_context = {
        'form': DeleteObjectForm,
        'delete_form_helper': DeleteFormHelper
    }
    template_name = "object_confirm_delete.html"
    success_message = (f'{_("product").capitalize()} '
                       f'{_("was deleted successfully")}')

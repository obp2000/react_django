"""
API endpoints that allow models to be viewed or edited.
"""
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from extra_views import (CreateWithInlinesView, NamedFormsetsMixin,
                         UpdateWithInlinesView)
from order_item.forms import OrderItemsFormSetHelper
from order_item.views import OrderItemInline
from react_django.forms import (DeleteFormHelper, DeleteObjectForm,
                                FilterFormHelper)

from .consts import GIFT_WEIGHT, PACKET_WEIGHT, SAMPLES_WEIGHT
from .filters import OrderFilter
from .forms import OrderForm, OrderFormHelper
from .models import Order
from .tables import OrderTable


class OrderListQuerysetMixin:
    queryset = Order.objects.list()


class OrderSuccessUrlMixin:
    success_url = reverse_lazy('order:list')


class OrderEditMixin(OrderSuccessUrlMixin):
    model = Order
    queryset = Order.objects.details()
    form_class = OrderForm
    template_name = "object_form.html"
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    extra_context = {
        'object_form_helper': OrderFormHelper,
        'order_items_formset_helper': OrderItemsFormSetHelper
    }

    def get_initial(self):
        return {
            'order_items_cost': getattr(self.object, 'order_items_cost', 0),
            'total_postals': getattr(self.object, 'total_postals', 0),
            'total_sum': getattr(self.object, 'total_sum', 0),
            'order_items_weight': getattr(self.object, 'order_items_weight', 0),
            'pindex': getattr(self.object, 'pindex', None),
            'gift_weight': GIFT_WEIGHT,
            'samples_weight': SAMPLES_WEIGHT,
            'packet_weight': PACKET_WEIGHT,
            'total_weight': getattr(self.object, 'total_weight', 0),
        }


class OrderList(OrderListQuerysetMixin, SingleTableMixin, FilterView):
    table_class = OrderTable
    table_pagination = {'per_page': 3}
    # template_name_suffix = '_list'
    # paginate_by = 3
    filterset_class = OrderFilter
    template_name = "object_list.html"
    extra_context = {
        'filter_helper':
        FilterFormHelper(filter_fields=OrderFilter._meta.fields),
        'delete_object_form': DeleteObjectForm,
        'delete_path_name': 'order:delete',
        'table_title': _("orders").capitalize(),
        'new_url': reverse_lazy('order:new'),
        'list_url': reverse_lazy('order:list')
    }


class OrderCreate(OrderEditMixin, SuccessMessageMixin, NamedFormsetsMixin,
                  CreateWithInlinesView):
    success_message = _(
        "order %(customer)s was created successfully").capitalize()


class OrderUpdate(OrderEditMixin, SuccessMessageMixin, NamedFormsetsMixin,
                  UpdateWithInlinesView):
    success_message = _(
        "order %(customer)s was updated successfully").capitalize()


class OrderDelete(OrderSuccessUrlMixin, OrderListQuerysetMixin,
                  BSModalDeleteView):
    # model = Order
    extra_context = {
        'form': DeleteObjectForm,
        'delete_form_helper': DeleteFormHelper
    }
    template_name = "object_confirm_delete.html"
    success_message = (f'{_("order").capitalize()} '
                       f'{_("was deleted successfully")}')

"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from bootstrap_modal_forms.generic import BSModalDeleteView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, \
                        NamedFormsetsMixin
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from react_django.forms import DeleteFormHelper, DeleteObjectForm, \
    FilterFormHelper
# from order_item.models import OrderItem
# from order_item.forms import OrderItemFormSetHelper
from order_item.views import OrderItemInline
from order_item.forms import OrderItemsFormSetHelper
from .serializers import OrderSerializer
from .models import Order, OrderQuerySet
from .forms import OrderForm, OrderFormHelper
from .tables import OrderTable
from .filters import OrderFilter


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.orders.list()
    serializer_class = OrderSerializer


class OrderList(SingleTableMixin, FilterView):
    queryset = Order.orders.list()
    table_class = OrderTable
    table_pagination = {'per_page': 3}
    # template_name_suffix = '_list'
    # paginate_by = 3
    filterset_class = OrderFilter
    template_name = "object_list.html"
    extra_context = {'filter_helper': FilterFormHelper(
        filter_fields=OrderFilter._meta.fields),
                     'delete_object_form': DeleteObjectForm,
                     'delete_path_name': 'order-delete',
                     'table_title': _("orders").capitalize(),
                     'new_url': reverse_lazy('order-new'),
                     'list_url': reverse_lazy('order-list')}


class OrderCreate(SuccessMessageMixin, NamedFormsetsMixin, CreateWithInlinesView):
    model = Order
    queryset = Order.orders.details()
    form_class = OrderForm
    template_name = "object_form.html"
    # fields = ['customer', 'sum']
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    success_message = _("order %(customer)s was created successfully").capitalize()
    extra_context = {'object_form_helper': OrderFormHelper,
                     'order_items_formset_helper': OrderItemsFormSetHelper}
    initial = {
        'gift_weight': OrderQuerySet.GIFT_WEIGHT,
        'samples_weight': OrderQuerySet.SAMPLES_WEIGHT,
        'packet_weight': OrderQuerySet.PACKET_WEIGHT,
        }


class OrderUpdate(SuccessMessageMixin, NamedFormsetsMixin, UpdateWithInlinesView):
    model = Order
    queryset = Order.orders.details()
    form_class = OrderForm
    template_name = "object_form.html"
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    success_message = _("order %(customer)s was updated successfully").capitalize()
    extra_context = {'object_form_helper': OrderFormHelper,
                     'order_items_formset_helper': OrderItemsFormSetHelper}

    def get_initial(self):
        return {
            'sum': self.object.sum,
            'total_postals': self.object.total_postals,
            'total_sum': self.object.total_sum,
            'weight': self.object.weight,
            'pindex': self.object.pindex,
            'gift_weight': OrderQuerySet.GIFT_WEIGHT,
            'samples_weight': OrderQuerySet.SAMPLES_WEIGHT,
            'packet_weight': OrderQuerySet.PACKET_WEIGHT,
            'total_weight': self.object.total_weight,
            }


class OrderDelete(BSModalDeleteView):
    model = Order
    extra_context = {'form': DeleteObjectForm,
                     'delete_form_helper': DeleteFormHelper}
    template_name = "object_confirm_delete.html"
    success_url = reverse_lazy('order-list')
    success_message = "%s %s" % (_("order").capitalize(), _("was deleted successfully"))

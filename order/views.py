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
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, \
                        NamedFormsetsMixin
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
# from order_item.models import OrderItem
# from order_item.forms import OrderItemFormSetHelper
from order_item.views import OrderItemInline
from .serializers import OrderSerializer
from .models import Order
from .forms import OrderForm, OrderFilterFormHelper, DeleteOrderForm
from .tables import OrderTable
from .filters import OrderFilter


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.orders.all_with_sum().select_related("customer")
    serializer_class = OrderSerializer


class OrderList(SingleTableMixin, FilterView):
    table_data = Order.orders.all_with_sum().select_related("customer")
    table_class = OrderTable
    table_pagination = {'per_page': 3}
    template_name_suffix = '_list'
    # paginate_by = 3
    filterset_class = OrderFilter
    extra_context = {'order_filter_helper': OrderFilterFormHelper,
                     'delete_order_form': DeleteOrderForm}


class OrderCreate(SuccessMessageMixin, NamedFormsetsMixin, 
                  CreateWithInlinesView):
    model = Order
    queryset = Order.orders.all_with_sum()
    form_class = OrderForm
    # fields = ['customer', 'sum']
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    success_message = _("№ %(id)s was created successfully")


class OrderUpdate(SuccessMessageMixin, NamedFormsetsMixin,
                  UpdateWithInlinesView):
    model = Order
    queryset = Order.orders.all_with_sum().select_related("customer", "customer__city")
    form_class = OrderForm
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    success_message = _("№ %(id)s was updated successfully")


class OrderDelete(BSModalDeleteView):
    model = Order
    extra_context = {'form': DeleteOrderForm}
    success_url = reverse_lazy('order-list')
    success_message = _("№ %(id)s: %(customer)s was deleted successfully")

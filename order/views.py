"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, \
                        NamedFormsetsMixin
# from order_item.models import OrderItem
# from order_item.forms import OrderItemFormSetHelper
from order_item.views import OrderItemInline
from .serializers import OrderSerializer
from .models import Order
from .forms import OrderForm


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.orders.all_with_sum()
    serializer_class = OrderSerializer


class OrderList(ListView):
    queryset = Order.orders.all_with_sum()
    paginate_by = 2


class OrderCreate(SuccessMessageMixin, CreateWithInlinesView):
    model = Order
    # form_class = OrderForm
    fields = '__all__'
    inlines = [OrderItemInline]
    # success_url = reverse_lazy('items:index')


class OrderUpdate(SuccessMessageMixin, NamedFormsetsMixin,
                  UpdateWithInlinesView):
    model = Order
    queryset = Order.orders.all_with_sum()
    form_class = OrderForm
    # fields = ['customer', 'sum']
    inlines = [OrderItemInline]
    inlines_names = ['order_items']
    # extra_context = {'order_items_helper': OrderItemFormSetHelper}
    success_message = "%s %s %s." % (_("order").title(),
                                     _("was updated"),
                                     _("successfully"))


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')

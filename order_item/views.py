from extra_views import InlineFormSetFactory

from .forms import BaseOrderItemInlineFormSet, OrderItemForm
from .models import OrderItem


class OrderItemInline(InlineFormSetFactory):
    model = OrderItem
    form_class = OrderItemForm
    formset_class = BaseOrderItemInlineFormSet

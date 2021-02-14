from extra_views import InlineFormSetFactory
from .models import OrderItem
from .forms import OrderItemForm, BaseOrderItemInlineFormSet


class OrderItemInline(InlineFormSetFactory):
    model = OrderItem
    form_class = OrderItemForm
    formset_class = BaseOrderItemInlineFormSet

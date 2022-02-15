from extra_views import InlineFormSetFactory

from .forms import OrderItemForm
from .models import OrderItem


class OrderItemInline(InlineFormSetFactory):
    model = OrderItem
    form_class = OrderItemForm

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        kwargs['queryset'] = OrderItem.objects.select_related("product__product_type")
        return kwargs

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs['extra'] = 1
        return kwargs

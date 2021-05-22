from extra_views import InlineFormSetFactory
from .models import OrderItem
from .forms import OrderItemForm, BaseOrderItemInlineFormSet


class OrderItemInline(InlineFormSetFactory):
    model = OrderItem
    form_class = OrderItemForm
    formset_class = BaseOrderItemInlineFormSet

    # def get_initial(self):
    #     return {
    #         'sum': self.object.sum,
    #         'one_m_weight': self.object.one_m_weight,
    #         'weight': self.object.weight,
    #         }

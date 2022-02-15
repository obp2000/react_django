from customer.widgets import CustomerWidget
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from react_django.forms import CharFieldDisabled

from .models import Order


class OrderForm(ModelForm):
    order_items_cost = CharFieldDisabled()
    total_postals = CharFieldDisabled()
    total_sum = CharFieldDisabled()
    order_items_weight = CharFieldDisabled()
    # pindex = CharFieldDisabled(label=_('pindex').capitalize())
    gift_weight = CharFieldDisabled()
    samples_weight = CharFieldDisabled(label=_('samples'))
    packet_weight = CharFieldDisabled()
    total_weight = CharFieldDisabled()

    class Media:
        js = ('js/order_form.js', )

    class Meta:
        model = Order
        exclude = ['products']
        widgets = {"customer": CustomerWidget}

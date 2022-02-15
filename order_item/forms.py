from django.forms import HiddenInput, ModelForm, NumberInput
from django.utils.translation import gettext_lazy as _
from product.widgets import ProductWidget
from react_django.forms import CharFieldDisabled

from .models import OrderItem


class OrderItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # print('kwargs', kwargs)
        if (instance := kwargs.get('instance', None)) and instance.id:
            kwargs['initial'] = {
                'cost': instance.cost,
                'weight': instance.weight,
                'one_m_weight': instance.one_m_weight,
            }
        super().__init__(*args, **kwargs)
        self.fields['product'].label.css_class = 'col-sm-7'
        self.fields['amount'].label.css_class = 'col-sm-1'

    cost = CharFieldDisabled(label=_('cost').title())
    weight = CharFieldDisabled(label=_('weight').title())
    one_m_weight = CharFieldDisabled(widget=HiddenInput())

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'amount', 'price', 'cost',
            'weight', 'one_m_weight']
        widgets = {
            "product": ProductWidget,
            "amount": NumberInput(attrs={'step': '0.05'}),
            # "price": NumberInput(attrs={ 'data_label_class': 'col-sm-4'})
        }

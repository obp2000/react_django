from django.forms.models import BaseInlineFormSet
from django.forms import ModelForm, HiddenInput, NumberInput
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from django_select2.forms import ModelSelect2Widget
from react_django.forms import CharFieldDisabled
from .models import OrderItem


class ProductWidget(ModelSelect2Widget):
    search_fields = ["name__icontains"]


class OrderItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'sum': instance.sum,
                                 'one_m_weight': instance.one_m_weight,
                                 'weight': instance.weight,}
        super().__init__(*args, **kwargs)
        self.fields['product'].label.css_class = 'col-sm-7'
        self.fields['amount'].label.css_class = 'col-sm-1'

    sum = CharFieldDisabled(label=_('sum').title())
    weight = CharFieldDisabled(label=_('weight').title())
    one_m_weight = CharFieldDisabled(widget=HiddenInput())

    class Meta:
        model = OrderItem
        fields = '__all__'
        widgets = {
            "product": ProductWidget,
            "amount": NumberInput(attrs={'step': '0.05'}),
            # "price": NumberInput(attrs={ 'data_label_class': 'col-sm-4'})
        }


class BaseOrderItemInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = OrderItem.order_items.list()
        # .select_related("product")
        super().__init__(*args, **kwargs)
        self.extra = 1


class OrderItemsFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'order_item/table_inline_formset.html'
        self.form_class = ''
        self.form_id = "order_items"
        self.form_tag = False
        self.count_post_cost_button = "<button class='btn btn-info btn-sm' \
            id='count_post_cost_button' type='button'>" + _('count').title() + "</button>"

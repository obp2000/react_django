# from django.forms import Media
from django.forms import ModelForm, DecimalField, IntegerField, CharField
from django.forms.widgets import NumberInput
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Layout, HTML, Row, MultiField,
                                 Fieldset, Column, Field)
from django_select2.forms import ModelSelect2Widget
# from ajax_select.helpers import make_ajax_field
# from ajax_select.fields import _media
# from .lookup import CustomerLookup
# from .forms_with_sums import FormWithSums
from .models import Order


class CustomerWidget(ModelSelect2Widget):
    search_fields = ["nick__icontains", "name__icontains"]


class FieldInRow(Field):

    def __init__(self, *args, **kwargs):
        # kwargs['css_class'] = 'col-sm-10'
        kwargs['wrapper_class'] = 'col-sm-4'
        super().__init__(*args, **kwargs)


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'sum': '%.2f' % instance.sum,
                                 'weight': instance.weight}
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        # self.helper.template = 'bootstrap4/table_inline_formset.html'
        # self.helper.form_tag = False

        self.helper.layout = Layout(
            Row(FieldInRow('customer')),
            Row(HTML("""<div class='form-group row col-sm-4'>
                      {{ order.customer.city.pindex }}&nbsp;
                      {{ order.customer.city.city }}&nbsp;
                      {{ order.customer.address }}
                      </div>""")),
            Row(FieldInRow('delivery_type'), FieldInRow('address')),
            # 'city__city',
            # HTML("{% load crispy_forms_tags %}"),
            HTML("{% load crispy_forms_tags %} \
                  {% crispy order_items %}"),
            Row(FieldInRow('gift')),
            Row(FieldInRow('packet')),
            Row(FieldInRow('post_cost')),
            Submit('submit', _('save').title())
        )

    # customer = make_ajax_field(Order, 'customer', 'customer')
    # customer = AutoCompleteSelectField('customer', required=False,
    #                                    label=('customer'),
    #                                    help_text=False)
    sum = CharField(required=False, disabled=True)
    weight = CharField(required=False, disabled=True)

    class Media:
        # extend = False
        js = ('order/js/scripts.js',)

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "customer": CustomerWidget
        }


# class OrderFormHelper(FormHelper):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.form_class = 'form-horizontal'
#         self.form_tag = False
#         # self.label_class = 'col-sm-2'
#         # self.field_class = 'col-sm-8'

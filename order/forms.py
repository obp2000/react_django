from django.forms import ModelForm, DecimalField, IntegerField, CharField, Form
from django.forms.widgets import NumberInput
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Row, MultiField, \
                                 Fieldset, Column, Div, Reset                    
from crispy_forms.bootstrap import FieldWithButtons, StrictButton, Field, \
                                    UneditableField, FormActions
from django_select2.forms import ModelSelect2Widget
from .models import Order


class CustomerWidget(ModelSelect2Widget):
    search_fields = ["nick__icontains", "name__icontains"]


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'sum': '{:.2f}'.format(instance.sum) if instance.sum else None,
                                 'total_postals': '{:.2f}'.format(instance.total_postals) if 
                                    instance.total_postals else None,
                                 'total_sum': '{:.2f}'.format(instance.total_sum) if instance.total_sum else None,
                                 'weight': instance.weight,
                                 'pindex': instance.customer.city.pindex if instance.customer and 
                                    instance.customer.city else None,
                                 'gift_weight': Order.GIFT_WEIGHT,
                                 'samples_weight': Order.SAMPLES_WEIGHT,
                                 'packet_weight': Order.PACKET_WEIGHT,
                                 'total_weight': instance.total_weight if instance.total_weight else None,
                                 }
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = "col-sm-2"
        self.helper.field_class = "col-sm-5"
        self.helper.layout = Layout(
            Fieldset(
                '{{ order }}',
                'customer',
                'pindex',
                Row(Column(HTML(_('city').capitalize()), css_class="col-sm-2"), 
                    Column(HTML("{{ order.customer.city.city }}"), css_id="city", css_class="col-sm-5")),
                Row(Column(HTML(_('address').capitalize()), css_class="col-sm-2"), 
                    Column(HTML("{{ order.customer.address }}"), css_id="customer_address", css_class="col-sm-5")),
                'delivery_type',
                'address'),
            HTML("{% load crispy_forms_tags %} {% crispy order_items %}"),
            Submit('submit', _('save').title())
        )

    sum = CharField(required=False, disabled=True)
    total_postals = CharField(required=False, disabled=True)
    total_sum = CharField(required=False, disabled=True)
    weight = CharField(required=False, disabled=True)
    pindex = CharField(required=False, disabled=True, label = _('pindex'))
    gift_weight = CharField(required=False, disabled=True)
    samples_weight = CharField(required=False, disabled=True, label = _('samples'))
    packet_weight = CharField(required=False, disabled=True)
    total_weight = CharField(required=False, disabled=True)

    class Media:
        js = ('order/js/order_form.js',)

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "customer": CustomerWidget
        }


class OrderFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'
        self.form_class = 'form-inline'
        self.field_template = 'bootstrap4/layout/inline_field.html'
        self.layout = Layout(
            'customer__nick',
            'customer__name',
            Submit('search', _('search').title())
        )


class DeleteOrderForm(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h3 class='modal-title'>%s</h3>" %  _('delete').capitalize()),
                Reset('dismiss', '&times;', css_class="btn-close", data_dismiss="modal", aria_label="Close"),
                css_class="modal-header"),
            Div(HTML("<p>%s <strong>{{ order }}</strong>?</p>" %  _('are you sure you want to delete').capitalize()), 
                css_class="modal-body"),
            Div(Submit('delete', _('Yes'), css_class="btn-danger"), css_class="modal-footer")
        )


    class Media:
        js = ('order/js/delete_order_form.js',)

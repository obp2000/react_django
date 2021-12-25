from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Fieldset, Layout, Row, Submit
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget
from react_django.forms import CharFieldDisabled

from .models import Order


class CustomerWidget(ModelSelect2Widget):
    search_fields = ["nick__icontains", "name__icontains"]


class OrderForm(ModelForm):

    sum = CharFieldDisabled()
    total_postals = CharFieldDisabled()
    total_sum = CharFieldDisabled()
    weight = CharFieldDisabled()
    pindex = CharFieldDisabled(label=_('pindex').capitalize())
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


class OrderFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.label_class = "col-sm-2"
        self.field_class = "col-sm-5"
        self.layout = Layout(
            Fieldset(
                """
                {% if order %}
                {{ order }} {{order.created_at}} (№{{order.id}})
                {% endif %}
                """, 'customer', 'pindex',
                Row(
                    Column(HTML(_('city').capitalize()), css_class="col-sm-2"),
                    Column(HTML("{{ order.customer.city.city }}"),
                           css_id="city",
                           css_class="col-sm-5")),
                Row(
                    Column(HTML(_('address').capitalize()),
                           css_class="col-sm-2"),
                    Column(HTML("{{ order.customer.address }}"),
                           css_id="customer_address",
                           css_class="col-sm-5")), 'delivery_type', 'address'),
            HTML("""
                {% load crispy_forms_tags %}
                {% crispy order_items order_items_formset_helper %}
                """), Submit('submit',
                             _('save').title()))

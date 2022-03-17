from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout
# from customer.models import Customer
# from django.utils.translation import gettext_lazy as _
from react_django.form_helpers import SaveButton


class OrderFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.label_class = "col-sm-2"
        self.field_class = "col-sm-9"
        self.layout = Layout(
            Fieldset(
                """
                {% if order %}
                    {{ order }} {{order.created_at}} (№{{order.id}})
                {% endif %}
                """,
                'customer',
                'address',
                'delivery_type',
                # Field('customer', css_class="fs-6"),
                # Row(
                #     Column(
                #         HTML(Customer._meta.get_field('address').verbose_name.capitalize()),
                #             css_class="form-group row col-sm-1"),
                #     Column(
                #         HTML("{{ order.customer.address }}"),
                #             css_id="customer_address",
                #             css_class="form-group row")),
                # Row(
                # Field('address', wrapper_class="col-sm-6"),
                # Field('delivery_type', css_class1="col-sm-7",
                #                            wrapper_class="col-sm-11")
                # )
            ),
            HTML(
                """
                {% load crispy_forms_tags %}
                {% crispy order_items order_items_formset_helper %}
                """
            ),
            SaveButton
        )

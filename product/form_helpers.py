from crispy_forms.bootstrap import InlineRadios, UneditableField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Field, Fieldset, Layout, Row
from react_django.form_helpers import SaveButton


class ProductFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.field_class = "col-sm-5"
        self.layout = Layout(
            Fieldset(
                '{{ object }}',
                UneditableField('id', css_class="col-sm-2"),
                'product_type',
                InlineRadios('threads'),
                InlineRadios('contents'),
                'fleece',
                'name',
                'image',
                HTML(
                    """{% if object.image %}
                            <img src='{{ object.image.url }}' width='100'
                                title='{{ object.name }}'/>
                            </br></br>
                       {% endif %}
                    """
                )
            ),
            Row(
                Field('price', css_class="col-sm-8", wrapper_class="col-sm-4"),
                Field('price_pre',
                      css_class="col-sm-8",
                      wrapper_class="col-sm-4"),
            ),
            Row(
                Field('density',
                      css_class="col-sm-8",
                      wrapper_class="col-sm-4"),
                Field('density_shop',
                      css_class="col-sm-8",
                      wrapper_class="col-sm-4")),
            Row(
                Field('width', css_class="col-sm-8", wrapper_class="col-sm-4"),
                Field('width_shop',
                      css_class="col-sm-8",
                      wrapper_class="col-sm-4"),
                # Column(HTML('{{ object.created_at }}'), css_class='col-sm-5')
            ),
            Row(
                Field('dollar_price',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
                Field('dollar_rate',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4")),
            Row(
                Field('price_rub_m',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
                Column(HTML(''), id='prices_with_coeffs',
                       css_class='col-sm-5')),
            Row(
                Field('weight_for_count',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
                Field('length_for_count',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
                Field('density_for_count',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4")),
            Row(
                Field('weight', css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
                Field('meters_in_roll',
                      css_class="col-sm-9",
                      wrapper_class="col-sm-4"),
            ),
            SaveButton
        )

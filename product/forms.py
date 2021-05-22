from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Row, \
                                 Fieldset, Column, Field
from crispy_forms.bootstrap import UneditableField, InlineRadios
from react_django.forms import CharFieldDisabled
from .models import Product


class ProductForm(ModelForm):

    id = CharFieldDisabled()
    price_rub_m = CharFieldDisabled(label=_('meter price').capitalize())
    density_for_count = CharFieldDisabled(label=_('density for count').capitalize())
    meters_in_roll = CharFieldDisabled(label=_('meters in roll').capitalize())

    def full_clean(self):
        if self.data.get('contents') == 'None' or self.data.get('threads') == 'None':
            data_copy = {}
            for key, value in self.data.items():
                if (key == 'contents' and value == 'None') or \
                   (key == 'threads' and value == 'None'):
                    data_copy[key] = ''
                else:
                    data_copy[key] = value
            self.data = data_copy
        super().full_clean()

    # def clean_contents(self):
    #     cd = self.cleaned_data
    #     print('ddddddddddd')
    #     print(cd['contents'])
    #     if cd['contents'] == 'None':
    #         return ''
    #     return cd['contents']

    class Media:
        js = ('product/js/product_form.js',)

    class Meta:
        model = Product
        fields = '__all__'


class ProductFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        # self.helper.label_class = "col-sm-1"
        self.field_class = "col-sm-5"
        self.layout = Layout(
            Fieldset('{{ object }}',
                     UneditableField('id', css_class="col-sm-2"),
                     'product_type',
                     InlineRadios('threads'),
                     InlineRadios('contents'),
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
                Field('price_pre', css_class="col-sm-8", wrapper_class="col-sm-4")
            ),
            Row(
                Field('density', css_class="col-sm-8", wrapper_class="col-sm-4"),
                Field('density_shop', css_class="col-sm-8", wrapper_class="col-sm-4")
            ),
            Row(
                Field('width', css_class="col-sm-8", wrapper_class="col-sm-4"),
                Field('width_shop', css_class="col-sm-8", wrapper_class="col-sm-4")
            ),
            Row(
                Field('dollar_price', css_class="col-sm-9", wrapper_class="col-sm-4"),
                Field('dollar_rate', css_class="col-sm-9", wrapper_class="col-sm-4")
            ),
            Row(
                Field('price_rub_m', css_class="col-sm-9", wrapper_class="col-sm-4"),
                Column(HTML(''), id='prices_with_coeffs', css_class='col-sm-5')
            ),
            Row(
                Field('weight_for_count', css_class="col-sm-9", wrapper_class="col-sm-4"),
                Field('length_for_count', css_class="col-sm-9", wrapper_class="col-sm-4"),
                Field('density_for_count', css_class="col-sm-9", wrapper_class="col-sm-4")
            ),
            Row(
                Field('weight', css_class="col-sm-9", wrapper_class="col-sm-4"),
                Field('meters_in_roll', css_class="col-sm-9", wrapper_class="col-sm-4"),
            ),
            Submit('submit', _('save').title())
        )

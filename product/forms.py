from django.forms import ModelForm, IntegerField, CharField
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Layout, HTML, Row, MultiField,
                                 Fieldset, Column, Field)
from crispy_forms.bootstrap import UneditableField
from .models import Product


class FieldInRow(Field):

    def __init__(self, *args, **kwargs):
        kwargs['css_class'] = 'col-sm-4'
        kwargs['wrapper_class'] = 'col-sm-5'
        super().__init__(*args, **kwargs)


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-sm-1'
        # self.helper.field_class = 'col-sm-7'
        # self.helper.template = 'bootstrap4/whole_uni_form.html'
        # self.helper.add_input(Submit('submit', _('save').title()))
        self.helper.layout = Layout(
            Fieldset('{{ object }}',
                     UneditableField('id'),
                     'name',
                     'image',
                     HTML("{% if object.image %}"
                          "<img src='{{ object.image.url }}'"
                          " width='100'"
                          " title='{{ object.name }}'/>"
                          "{% endif %}")),
            Row(FieldInRow('density'),
                FieldInRow('density_shop')),
            Row(FieldInRow('width'),
                FieldInRow('width_shop')),
            Row(FieldInRow('price'),
                FieldInRow('price_pre')),
            Submit('submit', _('save').title())
        )

    id = CharField(required=False, disabled=True)

    class Meta:
        model = Product
        fields = '__all__'

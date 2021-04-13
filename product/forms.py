from django.forms import ModelForm, IntegerField, CharField, Form
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Row, MultiField, \
                                 Fieldset, Column, Field, Div, Reset
from crispy_forms.bootstrap import UneditableField, FormActions
from .models import Product


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'price_rub_m': '{:.0f}'.format(instance.price_rub_m) if instance.price_rub_m else None,
                                 'density_for_count': '{:.0f}'.format(instance.density_for_count) if instance.density_for_count else None,
                                 'meters_in_roll': '{:.2f}'.format(instance.meters_in_roll) if instance.meters_in_roll else None
                                }
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = "col-sm-1"
        self.helper.field_class = "col-sm-5"
        self.helper.layout = Layout(
            Fieldset('{{ object }}',
                     UneditableField('id', css_class="col-sm-2"),
                     'name',
                     'image',
                     HTML(
                        """{% if object.image %} 
                                <img src='{{ object.image.url }}' width='100' title='{{ object.name }}'/>
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

    id = CharField(required=False, disabled=True)
    price_rub_m = CharField(required=False, disabled=True, label = _('meter price').capitalize())
    density_for_count = CharField(required=False, disabled=True, label = _('density for count').capitalize())
    meters_in_roll = CharField(required=False, disabled=True, label = _('meters in roll').capitalize())

    class Media:
        js = ('product/js/product_form.js',)

    class Meta:
        model = Product
        fields = '__all__'


class ProductFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'
        self.form_class = 'form-inline'
        self.field_template = 'bootstrap4/layout/inline_field.html'
        self.layout = Layout(
            'name',
            Submit('search', _('search').title())
        )


class DeleteProductForm(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h3 class='modal-title'>%s</h3>" % _('delete').capitalize()),
                Reset('dismiss', '&times;', css_class="btn-close", data_dismiss="modal", aria_label="Close"),
                css_class="modal-header"),
            Div(HTML("<p>%s <strong>{{ product.name }}</strong>?</p>" % _('are you sure you want to delete').capitalize()), 
                css_class="modal-body"),
            Div(Submit('delete', _('Yes'), css_class="btn-danger"), css_class="modal-footer")
        )


    class Media:
        js = ('product/js/delete_product_form.js',)
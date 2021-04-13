from django.forms import ModelForm, Form, CharField
from ajax_select.fields import AutoCompleteSelectField
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, HTML, Div, Reset
from crispy_forms.bootstrap import FormActions, InlineField
from django_select2.forms import ModelSelect2Widget
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Customer


class CityWidget(ModelSelect2Widget):
    search_fields = ["city__icontains"]


class CustomerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-1'
        self.helper.field_class = 'col-sm-5'
        self.helper.add_input(Submit('submit', _('save').title()))

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "city": CityWidget
        }


class CustomerFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'
        self.form_class = 'form-inline'
        self.field_template = 'bootstrap4/layout/inline_field.html'
        self.layout = Layout(
            'nick',
            'name',
            'city__city',
            Submit('search', _('search').title())
        )


class DeleteCustomerForm(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h3 class='modal-title'>%s</h3>" %  _('delete').capitalize()),
                Reset('dismiss', '&times;', css_class="btn-close", data_dismiss="modal", aria_label="Close"),
                css_class="modal-header"),
            Div(HTML("<p>%s <strong>{{ customer.nick }}</strong>?</p>" %  _('are you sure you want to delete').capitalize()), 
                css_class="modal-body"),
            Div(Submit('delete', _('Yes'), css_class="btn-danger"), css_class="modal-footer")
        )


    class Media:
        js = ('customer/js/delete_customer_form.js',)

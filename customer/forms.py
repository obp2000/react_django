from django.forms import ModelForm, Form, CharField
from ajax_select.fields import AutoCompleteSelectField
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, HTML
from crispy_forms.bootstrap import FormActions, InlineField
# from ajax_select.helpers import make_ajax_field
from .models import Customer
# from .lookup import CityLookup
from django_select2.forms import ModelSelect2Widget


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

    # name = CharField(max_length=20, help_text='20 characters max.', required=False)
    # city = AutoCompleteSelectField('city', required=False,
    #                                label=_('city'),
    #                                help_text=False)
    # city = make_ajax_field(Customer, 'city', 'city')

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
        test1 = "<a href='{% url 'customer-list' %}'>" + _('No').title() + \
            "</a>"
        self.helper.layout = Layout(
            HTML("<p>%s '{{ object }}'?</p>" % _('Delete')),
            FormActions(
                Submit('delete', _('Yes')),
                HTML(test1)
            )
        )

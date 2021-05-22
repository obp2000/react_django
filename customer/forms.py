from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML
from django_select2.forms import ModelSelect2Widget
from react_django.forms import CharFieldDisabled
from .models import Customer


class CityWidget(ModelSelect2Widget):
    search_fields = ["city__icontains"]


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ["nick", "name", "city", "address"]
        widgets = {
            "city": CityWidget
        }


class CustomerFormWitDisabledName(CustomerForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance and instance.id:
            kwargs['initial'] = {
                'name_disabled': instance.name
            }
        super().__init__(*args, **kwargs)

    name_disabled = CharFieldDisabled(label=_('name').capitalize())

    class Meta(CustomerForm.Meta):
        # print(CustomerForm.Meta.fields)
        # fields = ["nick", "name_disabled", "city", "address"]
        CustomerForm.Meta.fields.remove('name')
        fields = CustomerForm.Meta.fields


class CustomerFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.label_class = 'col-sm-1'
        self.field_class = 'col-sm-5'
        self.add_input(Submit('submit', _('save').title()))

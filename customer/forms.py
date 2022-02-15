from django.forms import ModelForm

from .models import Customer
from .widgets import CityWidget


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["nick", "name", "city", "address"]
        widgets = {"city": CityWidget}


# class CustomerFormWitDisabledName(CustomerForm):
#     def __init__(self, *args, **kwargs):
#         instance = kwargs.get('instance')
#         if instance and instance.id:
#             kwargs['initial'] = {'name_disabled': instance.name}
#         super().__init__(*args, **kwargs)

#     name_disabled = CharFieldDisabled(label=_('name'))

#     class Meta(CustomerForm.Meta):
#         # print(CustomerForm.Meta.fields)
#         # fields = ["nick", "name_disabled", "city", "address"]
#         # CustomerForm.Meta.fields.remove('name')
#         fields = CustomerForm.Meta.fields

from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _
from react_django.form_helpers import SaveButton


class CustomerFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.label_class = 'col-sm-1'
        self.field_class = 'col-sm-5'
        self.add_input(SaveButton)

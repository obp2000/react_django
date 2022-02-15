from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Layout, Reset, Submit
from django.utils.translation import gettext_lazy as _


class DeleteFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_media = False
        self.layout = Layout(
            Div(
                HTML((
                    f"""
                    <h5 class='modal-title'>
                        {_('are you sure you want to delete').capitalize()}?
                    </h5>
                    """)),
                Reset('dismiss', '&times;', css_class="btn-close",
                      data_dismiss="modal", aria_label="Close"),
                css_class="modal-header"
            ),
            Div(
                HTML("<h5>{{ object }}</h5>"),
                css_class="modal-body"
            ),
            Div(
                Submit('delete', _('Yes'), css_class="btn-danger"),
                css_class="modal-footer"
            )
        )


class FilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        filter_fields = kwargs.pop('filter_fields')
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'
        self.form_class = 'form-inline'
        self.field_template = 'bootstrap4/layout/inline_field.html'
        self.layout = Layout(
            *filter_fields,
            Submit('search', _('search').title()),
            HTML("&nbsp;"),
            HTML(
                "".join(["{% load bootstrap4 %} {% bootstrap_button '",
                 _('reset').capitalize(),
                 "' button_type='link' href=list_url %}"])
            )
        )


SaveButton = Submit('submit', _('save').title())

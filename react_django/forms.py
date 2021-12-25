from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Layout, Reset, Submit
from django.forms import CharField, Form
from django.utils.translation import gettext_lazy as _


class CharFieldDisabled(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["disabled"] = True
        kwargs["required"] = False
        super().__init__(*args, **kwargs)


class DeleteObjectForm(Form):

    class Media:
        js = ('js/delete_object_form.js',)


class DeleteFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_media = False
        self.layout = Layout(
            Div(HTML("<h5 class='modal-title'>%s?</h5>" %
                     _('are you sure you want to delete').capitalize()),
                Reset('dismiss', '&times;', css_class="btn-close",
                      data_dismiss="modal", aria_label="Close"),
                css_class="modal-header"),
            Div(HTML("<h5>{{ object }}</h5>"), css_class="modal-body"),
            Div(Submit('delete', _('Yes'), css_class="btn-danger"),
                css_class="modal-footer")
        )

# ResetFilterButton = HTML("{% load bootstrap4 %} {% load i18n %} \
#         {% trans 'reset'|capfirst as reset_title %} \
#         {% bootstrap_button reset_title button_type='link' href=list_url %}")


class FilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        filter_fields = kwargs.pop('filter_fields')
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'
        self.form_class = 'form-inline'
        self.field_template = 'bootstrap4/layout/inline_field.html'
        self.layout = Layout(
            # 'nick',
            # 'name',
            # 'city__city',
            *filter_fields,
            Submit('search', _('search').title()),
            HTML("&nbsp;"),
            HTML("{% load bootstrap4 %} {% bootstrap_button '" +
                 _('reset').capitalize() +
                 "' button_type='link' href=list_url %}")
        )

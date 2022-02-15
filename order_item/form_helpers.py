from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _


class OrderItemsFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'order_item/table_inline_formset.html'
        self.form_class = ''
        self.form_id = "order_items"
        self.form_tag = False
        self.count_post_cost_button = (
            "<button class='btn btn-info btn-sm "
            "id='count_post_cost_button' "
            f"type='button'>{_('count').title()}</button>")

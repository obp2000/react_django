from django.utils.translation import gettext_lazy as _

from ..forms import OrderForm
from ..models import Consts, Order

consts_data = {
    'name_singular': Order._meta.verbose_name.capitalize(),
    'name_plural': Order._meta.verbose_name_plural.capitalize(),
    'post_cost_with_packet': {'label': _('post cost with packet').capitalize()},
    'post_discount': {'label': _('post discount').capitalize()},
    'total_postals': {'label': OrderForm().fields['total_postals'].label},
    'total_sum': {'label': OrderForm().fields['total_sum'].label},
    'samples': {'label': _('samples').capitalize()},
    'Consts': Consts
    }

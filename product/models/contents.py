from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Contents(IntegerChoices):
    LYCRA = 0, _('with lycra')
    COTTON = 1, _('100% cotton')
    __empty__ = '----'

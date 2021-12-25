from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Packet(IntegerChoices):
    PACKET25 = 25, '25'
    PACKET27 = 27, '27'
    PACKET50 = 50, '50'
    PACKET55 = 55, '55'
    PACKET72 = 72, '72'
    PACKET85 = 85, '85'
    __empty__ = _('(Unknown)')

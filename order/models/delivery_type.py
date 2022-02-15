from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class DeliveryType(IntegerChoices):
    POST = 0, _('Post of Russia')
    DEL_LIN = 1, _('Business Lines')
    PEK = 2, _('PEK')
    GTD = 3, _('GTD (Whale)')
    ENERGIA = 4, _('Energy')
    GDE = 5, _('Railway Expedition')
    RATEK = 6, _('Ratek')
    BAIKAL = 7, _('Baikal Service')
    SDEK_P = 8, _('SDEK Parcel')
    __empty__ = '----'

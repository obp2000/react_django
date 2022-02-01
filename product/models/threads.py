from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Threads(IntegerChoices):
    TWO_THREADS = 0, _('two threads')
    THREE_THREADS = 1, _('three threads')
    __empty__ = '----'

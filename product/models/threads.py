from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Threads(IntegerChoices):
    TWO_THREADS = 1, _('two threads')
    THREE_THREADS = 2, _('three threads')

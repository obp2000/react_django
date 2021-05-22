from django.db.models import Model, CharField
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


class City(Model):
    pindex = CharField(_('pindex'), primary_key=True, max_length=6)
    city = CharField(pgettext_lazy('city name', 'name'), unique=True, max_length=80)

    class Meta:
        ordering = ['city']
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        # indexes = [
        #     Index(fields=['city',]),
        # ]

    def __str__(self):
        return self.city

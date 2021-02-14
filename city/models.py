from django.db.models import Model, CharField
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


class City(Model):
    pindex = CharField(_('index'), primary_key=True, max_length=6)
    city = CharField(pgettext_lazy('city name', 'name'), unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'cities'
        ordering = ['city']
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return self.city

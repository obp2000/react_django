from django.db.models import CharField, Model
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


class City(Model):
    pindex = CharField(_('pindex'), max_length=6, null=True, blank=True)
    city = CharField(pgettext_lazy('city name', 'name'), max_length=80)
    # pindex = CharField(max_length=6, blank=True, null=True)
    opsname = CharField(max_length=60, blank=True, null=True)
    # citykey = CharField(max_length=80, blank=True, null=True)
    # geo_lat = DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # geo_long = DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    address = CharField(max_length=512, blank=True, null=True)
    # json_dlvlim = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        index_together = [
            ["city", "pindex"]
        ]
        ordering = ['city', 'pindex']
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        # indexes = [
        #     Index(fields=['city',]),
        # ]

    def __str__(self):
        return self.city

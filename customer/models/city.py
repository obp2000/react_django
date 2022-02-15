from django.db.models import CharField, Model
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import pgettext_lazy
from react_django.utils import make_label


class City(Model):
    pindex = CharField(_('pindex'), max_length=6, null=True, blank=True)
    city = CharField(_('city'), max_length=80)
    opsname = CharField(max_length=60, blank=True, null=True)
    address = CharField(max_length=512, blank=True, null=True)

    def pindex_label(self):
        return (f"{City._meta.get_field('pindex').verbose_name[:3]}."
                f"{self.pindex}")

    def city_label(self):
        return (f"{City._meta.verbose_name[:1]}."
                f"{self.city}")

    def long_str(self):
        labels_map = {'pindex': self.pindex_label,
                      'city': self.city_label}
        return make_label(self, labels_map)

    class Meta:
        index_together = [
            ["city", "pindex"]
        ]
        ordering = ['city', 'pindex']
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
       return self.city

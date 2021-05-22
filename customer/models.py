from django.db.models import Model, CharField, DateTimeField, ForeignKey, \
    SET_NULL
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from city.models import City


class Customer(Model):
    nick = CharField(_('nick'), max_length=255)
    name = CharField(_('name'), max_length=255, blank=True)
    city = ForeignKey(City, SET_NULL, blank=True, null=True,
                      db_column='pindex', verbose_name=_('city'))
    address = CharField(_('address'), max_length=255, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    def get_absolute_url(self):
        return reverse('customer:customer-update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nick']
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        permissions = [
            ("change_customer_name", "Can change the name of customers"),
            ("change_customer_city", "Can change the city of customers"),
        ]

    def __str__(self):
        return "%s (%s)" % (self.nick, self.name,)

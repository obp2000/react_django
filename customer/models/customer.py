from django.db.models import (SET_NULL, CharField, DateTimeField, ForeignKey,
                              Model)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .city import City


class Customer(Model):
    nick = CharField(_('nick'), max_length=255)
    name = CharField(_('name'), max_length=255, blank=True)
    # city = ForeignKey(City,
    #                   SET_NULL,
    #                   blank=True,
    #                   null=True,
    #                   db_column='pindex',
    #                   verbose_name=_('city'))
    city = ForeignKey(City,
                      SET_NULL,
                      blank=True,
                      null=True,
                      # related_name="cities1",
                      # db_column='city_id',
                      verbose_name=_('city'))
    address = CharField(_('address'), max_length=255, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    def get_absolute_url(self):
        return reverse('customer:update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        permissions = [
            ("change_customer_name", "Can change the name of customers"),
            ("change_customer_city", "Can change the city of customers"),
        ]

    def __str__(self):
        return f'{self.nick} ({self.name})' if self.name else self.nick

from django.db.models import (SET_NULL, CharField, DateTimeField, ForeignKey,
                              Model)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from react_django.utils import make_label

from .city import City


class Customer(Model):
    nick = CharField(_('nick'), max_length=255)
    name = CharField(_('name'), max_length=255, blank=True)
    city = ForeignKey(City,
                      SET_NULL,
                      blank=True,
                      null=True)
    address = CharField(_('address'), max_length=255, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    def get_absolute_url(self):
        return reverse('customer:update', kwargs={'pk': self.pk})

    def name_label(self):
        return (f"{Customer._meta.get_field('name').verbose_name}:"
                f"{self.name}")

    def city_label(self):
        return self.city.long_str()

    def address_label(self):
        return (f"{Customer._meta.get_field('address').verbose_name}: "
                f"{self.address}")

    def long_str(self):
        labels_map = {'nick': self.nick,
                      'name': self.name_label,
                      'city': self.city_label,
                      'address': self.address_label}
        return make_label(self, labels_map)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        permissions = [
            ("change_customer_name", "Can change the name of customers"),
            ("change_customer_city", "Can change the city of customers"),
        ]

    def __str__(self):
        labels_map = {'nick': self.nick,
                      'name': f"({self.name})"}
        return make_label(self, labels_map)

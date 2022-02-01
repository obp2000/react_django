from customer.models import Customer
from django.db.models import (SET_NULL, CharField, DateTimeField, ForeignKey,
                              IntegerField, ManyToManyField, Model,
                              PositiveIntegerField)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from order_item.models import OrderItem
from product.models import Product

from .delivery_type import DeliveryType
from .managers import OrderManager
from .packet import Packet


class Order(Model):
    customer = ForeignKey(Customer,
                          SET_NULL,
                          null=True,
                          verbose_name=_('customer'))
    post_cost = PositiveIntegerField(_('post_cost'), default=0, blank=True)
    packet = PositiveIntegerField(_('packet'),
                                  choices=Packet.choices,
                                  blank=True,
                                  null=True)
    delivery_type = IntegerField(_('delivery_type'),
                                 choices=DeliveryType.choices,
                                 blank=True,
                                 null=True)
    address = CharField(_('address'), max_length=255, blank=True)
    gift = CharField(_('gift'), max_length=255, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)
    # products = ManyToManyField(Product,
    #                            through="order_item.OrderItem",
    #                            blank=True)

    # orders = OrderManager()
    objects = OrderManager()

    def get_absolute_url(self):
        return reverse('order:update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return (f'{self._meta.verbose_name.capitalize()} '
                f'{_("from")} {self.customer}')

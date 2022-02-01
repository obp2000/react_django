from django.db.models import (CASCADE, SET_NULL, DateTimeField, DecimalField,
                              ForeignKey, Model, PositiveIntegerField)
from django.utils.translation import gettext_lazy as _
from order.models import Order
from product.models import Product

from .managers import OrderItemManager


class OrderItem(Model):
    order = ForeignKey(Order, CASCADE, null=True, related_name='order_items',
                       verbose_name=_('order'))
    product = ForeignKey(Product, SET_NULL, null=True, blank=True,
                         verbose_name=_('product'))
    amount = DecimalField(_('amount'), max_digits=5, decimal_places=2,
                          default=0, blank=True)
    price = PositiveIntegerField(_('price'), default=0, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    # order_items = OrderItemManager()
    objects = OrderItemManager()

    class Meta:
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')

    # @property
    # def cost(self):
    #     return self.price * self.amount

    # @property
    # def weight(self):
    #     if (self.amount and self.product and self.product.one_m_weight):
    #         return int(self.amount * self.product.one_m_weight)
    #     else:
    #         return 0

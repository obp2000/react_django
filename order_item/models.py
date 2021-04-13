# from django.db.models import (Model, DateTimeField, DecimalField,
#                               ForeignKey, SET_NULL, CASCADE)
from django.db.models import Model, DateTimeField, DecimalField, \
    PositiveIntegerField, IntegerField, ForeignKey, SET_NULL, \
    CASCADE, Sum, F, QuerySet, Manager
from django.utils.translation import gettext_lazy as _
from product.models import Product
from order.models import Order


class OrderItemQuerySet333(QuerySet):

    # def all_with_sum1(self):
    #     return self.annotate(sum=Sum(F('price') *
    #                                  F('amount')),
    #                          weight=Sum(F('amount') *
    #                                     F('product__density') *
    #                                     F('product__width') /
    #                                     100,
    #                                     output_field=IntegerField(blank=True)))

    def all_with_sum(self):
        return self.annotate(density=F('product__density'),
                             width=F('product__width'),
                             one_m_weight=F('density') *
                                          F('width') / 100,
                             weight=F('amount') * F('one_m_weight'))


class OrderItem(Model):
    order = ForeignKey(Order, CASCADE, related_name='order_items',
                       blank=True, verbose_name=_('order'))
    product = ForeignKey(Product, SET_NULL, blank=True, null=True,
                         verbose_name=_('product'))
    amount = DecimalField(_('amount'), max_digits=5, decimal_places=2,
                          blank=True, null=True, default=0)
    price = PositiveIntegerField(_('price'), blank=True, null=True, default=0)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    # objects = Manager()
    # order_items = OrderItemQuerySet.as_manager()

    @property
    def sum(self):
        return (self.price or 0) * (self.amount or 0)
    # sum.blank = True
    # sum.verbose_name = _('sum')
    # sum = property(sum)

    @property
    def density(self):
        return self.product.density if self.product else None

    @property
    def width(self):
        return self.product.width if self.product else None

    @property
    def one_m_weight(self):
        return int(self.density * self.width / 100) if self.density and self.width else None

    @property
    def weight(self):
        return int(self.amount * self.one_m_weight) if self.one_m_weight else None


    class Meta:
        managed = False
        db_table = 'order_items'
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')

# from django.db.models import (Model, DateTimeField, DecimalField,
#                               ForeignKey, SET_NULL, CASCADE)
from django.db.models import Model, DateTimeField, DecimalField, \
    PositiveIntegerField, ForeignKey, SET_NULL, \
    CASCADE, Sum, F, QuerySet, Manager
from django.utils.translation import gettext_lazy as _
from product.models import Product
from order.models import Order


# class OrderItemQuerySet(QuerySet):

#     def all_with_sum(self):
#         return self.annotate(sum=Sum(F('price') *
#                                      F('amount')),
#                              weight=Sum(F('amount') *
#                                         F('product__density') *
#                                         F('product__width') /
#                                         100,
#                                         output_field=IntegerField(blank=True)))

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

    @property
    def sum(self):
        return self.price * self.amount
    # sum.blank = True
    # sum.verbose_name = _('sum')
    # sum = property(sum)

    @property
    def weight(self):
        if self.product and self.product.density and self.product.width:
            return int(self.amount * self.product.density *
                       self.product.width / 100)
        else:
            return 0
    # weight.blank = True
    # weight.verbose_name = _('weight')
    # weight = property(weight)

    @property
    def density(self):
        if self.product and self.product.density:
            return self.product.density
        else:
            return 0

    @property
    def width(self):
        if self.product and self.product.width:
            return self.product.width
        else:
            return 0

    # objects = Manager()
    # order_items = OrderItemQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'order_items'
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')

from django.db.models import Model, DateTimeField, DecimalField, \
    PositiveIntegerField, IntegerField, ForeignKey, SET_NULL, \
    CASCADE, F, QuerySet, ExpressionWrapper
from django.utils.translation import gettext_lazy as _
from product.models import Product
from order.models import Order


class OrderItemQuerySet(QuerySet):

    one_m_weight = ExpressionWrapper(F('product__density') * F('product__width') / 100,
                                     output_field=IntegerField())

    sum = ExpressionWrapper(F('price') * F('amount'), output_field=DecimalField(decimal_places=2))

    weight = ExpressionWrapper(F('amount') * F('one_m_weight'), output_field=IntegerField())

    def list(self):
        return self.select_related("product").annotate(
            one_m_weight=self.one_m_weight,
            weight=self.weight,
            sum=self.sum)


class OrderItem(Model):
    order = ForeignKey(Order, CASCADE, null=True, related_name='order_items',
                       verbose_name=_('order'))
    product = ForeignKey(Product, SET_NULL, null=True, verbose_name=_('product'))
    amount = DecimalField(_('amount'), max_digits=5, decimal_places=2, default=0)
    price = PositiveIntegerField(_('price'), default=0)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    order_items = OrderItemQuerySet.as_manager()

    class Meta:
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')

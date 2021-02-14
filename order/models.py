from django.db.models import Model, CharField, IntegerField, \
    PositiveIntegerField, DateTimeField, ForeignKey, SET_NULL, \
    DecimalField, Sum, F, QuerySet, Manager, IntegerChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from delivery_type.models import DeliveryType


class Packet(IntegerChoices):
    PACKET25 = 25, '25'
    PACKET27 = 27, '27'
    PACKET50 = 50, '50'
    PACKET55 = 55, '55'
    PACKET72 = 72, '72'
    PACKET85 = 85, '85'
    __empty__ = _('(Unknown)')


class OrderQuerySet(QuerySet):
    def all_with_sum(self):
        return self.annotate(sum=Sum(F('order_items__price') *
                                     F('order_items__amount'),
                                     output_field=DecimalField(blank=True)),
                             weight=Sum(F('order_items__amount') *
                                        F('order_items__product__density') *
                                        F('order_items__product__width') /
                                        100,
                                        output_field=IntegerField(blank=True)))


class Order(Model):
    customer = ForeignKey(Customer, SET_NULL, blank=True, null=True,
                          verbose_name=_('customer'))
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)
    post_cost = PositiveIntegerField(_('post_cost'), blank=True, null=True)
    packet = PositiveIntegerField(_('packet'), choices=Packet.choices,
                                  blank=True, null=True)
    delivery_type = IntegerField(_('delivery_type'),
                                 choices=DeliveryType.choices, blank=True,
                                 null=True)
    address = CharField(_('address'), max_length=255, blank=True)
    gift = CharField(_('gift'), max_length=255, blank=True)

    objects = Manager()
    orders = OrderQuerySet.as_manager()

    # @classmethod
    # def test1(cls):
    #     return cls.objects.annotate(sum=Sum(F('order_items__price')
    #                                 * F('order_items__amount')))

    def get_absolute_url(self):
        return reverse('order-update', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'orders'
        ordering = ['-created_at']
        verbose_name = _('order')
        verbose_name_plural = _('orders')

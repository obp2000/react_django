from django.db.models import Model, CharField, IntegerField, \
    PositiveIntegerField, DateTimeField, ForeignKey, SET_NULL, \
    Sum, F, QuerySet, IntegerChoices, \
    ExpressionWrapper, Case, When, ManyToManyField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import dateformat
from django.conf.locale.ru.formats import DATETIME_FORMAT
# from decimal import Decimal
from customer.models import Customer
# from order_item.models import OrderItem
from product.models import Product
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

    SUM_FOR_POST_DISCOUNT = 1000
    POST_DISCOUNT_PERCENT = 30
    SUM_FOR_GIFT = 2000
    GIFT_WEIGHT = 100
    PACKET_WEIGHT = 50
    SAMPLES_WEIGHT = 50

    sum = Sum(F('order_items__price') * F('order_items__amount'), output_field=IntegerField())

    weight = Sum(F('order_items__amount') * F('order_items__product__density') *
                 F('order_items__product__width') / 100, output_field=IntegerField())

    post_cost_with_packet = ExpressionWrapper(F('post_cost') + F('packet'),
                                              output_field=IntegerField())

    post_discount = Case(When(sum__gte=SUM_FOR_POST_DISCOUNT,
                              then=F('post_cost_with_packet') * (POST_DISCOUNT_PERCENT / 100)),
                         output_field=IntegerField())

    total_postals = ExpressionWrapper(F('post_cost_with_packet') - F('post_discount'),
                                      output_field=IntegerField())

    total_sum = ExpressionWrapper(F('sum') + F('total_postals'), output_field=IntegerField())

    need_gift = Case(When(sum__gte=SUM_FOR_GIFT, then=True))

    gift_weight = Case(When(need_gift, then=GIFT_WEIGHT), output_field=IntegerField())

    total_weight = ExpressionWrapper(F('weight') + F('gift_weight') +
                                     PACKET_WEIGHT + SAMPLES_WEIGHT, output_field=IntegerField())
    pindex = F('customer__city__pindex')

    def list(self):
        return self.select_related("customer__city").annotate(
            sum=self.sum).order_by('-created_at')

    def details(self):
        return self.select_related("customer__city").annotate(
            sum=self.sum,
            weight=self.weight,
            post_cost_with_packet=self.post_cost_with_packet,
            post_discount=self.post_discount,
            total_postals=self.total_postals,
            total_sum=self.total_sum,
            need_gift=self.need_gift,
            gift_weight=self.gift_weight,
            total_weight=self.total_weight,
            pindex=self.pindex)


class Order(Model):
    customer = ForeignKey(Customer, SET_NULL, null=True, verbose_name=_('customer'))
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)
    post_cost = PositiveIntegerField(_('post_cost'), default=0)
    packet = PositiveIntegerField(_('packet'), choices=Packet.choices,
                                  blank=True, null=True)
    delivery_type = IntegerField(_('delivery_type'), choices=DeliveryType.choices,
                                 blank=True, null=True)
    address = CharField(_('address'), max_length=255, blank=True)
    gift = CharField(_('gift'), max_length=255, blank=True)
    products = ManyToManyField(Product, through="order_item.OrderItem")

    # objects = Manager()
    orders = OrderQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('order-update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return "%s №%s %s %s" % (self._meta.verbose_name.capitalize(),
                                   self.id,
                                   _('from'),
                                   dateformat.format(self.created_at, DATETIME_FORMAT),)

from django.db.models import (BooleanField, Case, DecimalField,
                              ExpressionWrapper, F, IntegerField, QuerySet,
                              Sum, When)

from .consts import Consts


class OrderQuerySet(QuerySet):

    # Consts = {'SUM_FOR_POST_DISCOUNT': 1000,
    #           'POST_DISCOUNT_PERCENT': 30,
    #           'SUM_FOR_GIFT': 2000,
    #           'GIFT_WEIGHT': 100,
    #           'PACKET_WEIGHT': 50,
    #           'SAMPLES_WEIGHT': 50}

    order_items_amount = Sum(('order_items__amount'),
              output_field=DecimalField(max_digits=5, decimal_places=2))

    order_items_cost = Sum(F('order_items__price') * F('order_items__amount'),
              output_field=DecimalField(max_digits=7, decimal_places=2))

    order_items_weight = Sum(F('order_items__amount') *
                 F('order_items__product__density') *
                 F('order_items__product__width') / 100,
                 output_field=IntegerField())

    post_cost_with_packet = Case(When(packet__gt=0,
                                      then=F('post_cost') + F('packet')),
                                 default=F('post_cost'),
                                 output_field=IntegerField())

    post_discount = Case(When(order_items_cost__gte=Consts['SUM_FOR_POST_DISCOUNT'],
                              then=F('post_cost_with_packet') *
                              (Consts['POST_DISCOUNT_PERCENT'] / 100)),
                         default=0,
                         output_field=IntegerField())

    total_postals = ExpressionWrapper(F('post_cost_with_packet') -
                                      F('post_discount'),
                                      output_field=IntegerField())

    total_sum = ExpressionWrapper(F('order_items_cost') + F('total_postals'),
                                  output_field=IntegerField())

    need_gift = Case(When(order_items_cost__gte=Consts['SUM_FOR_GIFT'],
                          then=True),
                     output_field=BooleanField())

    gift_weight = Case(When(need_gift, then=Consts['GIFT_WEIGHT']),
                       default=0,
                       output_field=IntegerField())

    total_weight = ExpressionWrapper(F('order_items_weight') + F('gift_weight') +
                                     Consts['PACKET_WEIGHT'] +
                                     Consts['SAMPLES_WEIGHT'],
                                     output_field=IntegerField())

    pindex = F('customer__city__pindex')

    def list(self):
        return self.select_related("customer__city").annotate(
            order_items_cost=self.order_items_cost).order_by('-created_at')

    def details(self):
        return self.select_related("customer__city").prefetch_related('order_items').annotate(
              order_items_amount=self.order_items_amount,
              order_items_cost=self.order_items_cost,
              order_items_weight=self.order_items_weight,
              post_cost_with_packet=self.post_cost_with_packet,
              post_discount=self.post_discount,
              total_postals=self.total_postals,
              total_sum=self.total_sum,
              need_gift=self.need_gift,
              gift_weight=self.gift_weight,
              total_weight=self.total_weight,
              pindex=self.pindex).order_by('-created_at')


OrderManager = OrderQuerySet.as_manager

from django.db.models import (BooleanField, Case, ExpressionWrapper, F,
                              IntegerField, QuerySet, Sum, When)

from ..consts import (GIFT_WEIGHT, PACKET_WEIGHT, POST_DISCOUNT_PERCENT,
                      SAMPLES_WEIGHT, SUM_FOR_GIFT, SUM_FOR_POST_DISCOUNT)


class OrderQuerySet(QuerySet):

    sum = Sum(F('order_items__price') * F('order_items__amount'),
              output_field=IntegerField())

    weight = Sum(F('order_items__amount') *
                 F('order_items__product__density') *
                 F('order_items__product__width') / 100,
                 output_field=IntegerField())

    post_cost_with_packet = Case(When(packet__gt=0,
                                      then=F('post_cost') + F('packet')),
                                 default=F('post_cost'),
                                 output_field=IntegerField())

    post_discount = Case(When(sum__gte=SUM_FOR_POST_DISCOUNT,
                              then=F('post_cost_with_packet') *
                              (POST_DISCOUNT_PERCENT / 100)),
                         default=0,
                         output_field=IntegerField())

    total_postals = ExpressionWrapper(F('post_cost_with_packet') -
                                      F('post_discount'),
                                      output_field=IntegerField())

    total_sum = ExpressionWrapper(F('sum') + F('total_postals'),
                                  output_field=IntegerField())

    need_gift = Case(When(sum__gte=SUM_FOR_GIFT, then=True),
                     output_field=BooleanField())

    gift_weight = Case(When(need_gift, then=GIFT_WEIGHT),
                       default=0,
                       output_field=IntegerField())

    total_weight = ExpressionWrapper(F('weight') + F('gift_weight') +
                                     PACKET_WEIGHT + SAMPLES_WEIGHT,
                                     output_field=IntegerField())

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


OrderManager = OrderQuerySet.as_manager

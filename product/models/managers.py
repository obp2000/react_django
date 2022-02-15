from django.db.models import (Case, DecimalField, ExpressionWrapper, F,
                              IntegerField, QuerySet, When)


class ProductQuerySet(QuerySet):
    one_m_weight = ExpressionWrapper(F('density') * F('width') / 100,
                                     output_field=IntegerField())

    price_rub_m = ExpressionWrapper(F('dollar_price') * F('dollar_rate') *
                                    F('one_m_weight') / 1000,
                                    output_field=IntegerField())

    density_for_count = Case(When(length_for_count__gt=0,
                                  width__gt=0,
                                  then=F('weight_for_count') /
                                  F('length_for_count') / F('width') * 100),
                             output_field=IntegerField())

    meters_in_roll = Case(When(one_m_weight__gt=0,
                               then=F('weight') * 1000 / F('one_m_weight')),
                          output_field=DecimalField(decimal_places=2))

    def details(self):
        return self.select_related('product_type').annotate(
            one_m_weight=self.one_m_weight,
            price_rub_m=self.price_rub_m,
            density_for_count=self.density_for_count,
            meters_in_roll=self.meters_in_roll)


ProductManager = ProductQuerySet.as_manager

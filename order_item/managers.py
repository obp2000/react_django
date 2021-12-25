from django.db.models import (DecimalField, ExpressionWrapper, F, IntegerField,
                              QuerySet)


class OrderItemQuerySet(QuerySet):
    one_m_weight = ExpressionWrapper(F('product__density') *
                                     F('product__width') / 100,
                                     output_field=IntegerField())

    sum = ExpressionWrapper(F('price') * F('amount'),
                            output_field=DecimalField(decimal_places=2))

    weight = ExpressionWrapper(F('amount') * F('one_m_weight'),
                               output_field=IntegerField())

    def list(self):
        return self.select_related("product").annotate(
            one_m_weight=self.one_m_weight, weight=self.weight, sum=self.sum)


OrderItemManager = OrderItemQuerySet.as_manager

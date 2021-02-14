# from django.db.models import Q
from ajax_select import register, LookupChannel
from product.models import Product


@register('product')
class ProductLookup(LookupChannel):
    model = Product

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q)

    def format_item_display(self, item):
        return u"""<span class='tag' 
                   data-price='%s' 
                   data-density='%s' 
                   data-width='%s'>%s</span>""" % (item.price,
                                                   item.density,
                                                   item.width,
                                                   item.name,)

    def check_auth(self, request):
        return True

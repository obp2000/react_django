"""
Autocomplete customer.
"""
from django.db.models import Q
from ajax_select import register, LookupChannel
# from django.forms import Media
from customer.models import Customer


@register('customer')
class CustomerLookup(LookupChannel):
    """
    Lookup customer.
    """
    model = Customer

    def get_query(self, q, request):
        return self.model.objects.filter(Q(nick__icontains=q) |
                                         Q(name__icontains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s (%s)</span>" % (item.nick, item.name)

    def check_auth(self, request):
        return True

    # class Media:
    #     js = ('order/js/scripts.js',)
    # @property
    # def media(self):
    #     return self.media + Media(js=('order/js/scripts.js'))

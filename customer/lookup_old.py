from ajax_select import register, LookupChannel
from city.models import City


@register('city')
class CityLookup(LookupChannel):
    model = City

    def get_query(self, q, request):
        return self.model.objects.filter(city__icontains=q)

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.city

    def check_auth(self, request):
        return True

from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget


class CityWidget(ModelSelect2Widget):
    search_fields = ["pindex__icontains", "city__icontains"]

    def label_from_instance(self, obj):
        return obj.long_str()


class CustomerWidget(ModelSelect2Widget):
    search_fields = ["nick__icontains", "name__icontains",
        "city__city__icontains", "city__pindex__icontains",
        "address__icontains"]

    def label_from_instance(self, obj):
        return obj.long_str()

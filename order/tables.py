from django.utils.translation import gettext_lazy as _
from django_tables2 import Column, Table, TemplateColumn

from .models import Order


class OrderTable(Table):

    id = Column(linkify=True)
    sum = Column(linkify=True, verbose_name=_('sum').capitalize())
    delete = TemplateColumn(template_name="delete_column.html",
                            verbose_name='')

    class Meta:
        model = Order
        fields = ["id", "customer", "sum", "created_at", "updated_at"]
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class":
            "table table-striped table-sm border-info table-hover shadow"
        }

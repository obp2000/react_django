from django_tables2 import Table, Column, LinkColumn, A, TemplateColumn
from django.utils.translation import gettext_lazy as _
from .models import Product


class ProductTable(Table):

    id = Column(linkify=True)
    name = Column(linkify=True)
    delete = TemplateColumn(template_name="product/delete_column.html", verbose_name='')

    class Meta:
        model = Product
        fields = ["id", "name", "price", "width", "density", "created_at", "updated_at"]
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class":
                 "table table-primary table-striped table-sm border-info table-hover"}

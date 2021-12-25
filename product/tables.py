from django_tables2 import Column, Table, TemplateColumn

from .models import Product


class ProductTable(Table):

    id = Column(linkify=True)
    # product_type = Column(linkify=True)
    name = Column(linkify=True)
    width = Column(attrs={"td": {"class": "text-muted"}})
    density = Column(attrs={"td": {"class": "text-muted"}})
    created_at = Column(attrs={"td": {"class": "text-muted"}})
    updated_at = Column(attrs={"td": {"class": "text-muted"}})
    delete = TemplateColumn(template_name="delete_column.html",
                            verbose_name='')

    class Meta:
        model = Product
        fields = [
            "id", "product_type", "contents", "threads", "name", "price",
            "width", "density", "created_at", "updated_at"
        ]
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class":
            "table table-striped table-sm border-info shadow table-hover"
        }

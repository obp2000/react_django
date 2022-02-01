from django_tables2 import Column, Table, TemplateColumn

# from django_tables2 import A  # alias for Accessor
from .models import Customer


class CustomerTable(Table):

    nick = Column(linkify=True)
    name = Column(linkify=True)
    city = Column(attrs={"td": {"class": "text-muted"}})
    city__pindex = Column(attrs={"td": {"class": "text-muted"}})
    created_at = Column(attrs={"td": {"class": "text-muted"}})
    delete = TemplateColumn(template_name="delete_column.html",
                            verbose_name='')

    class Meta:
        model = Customer
        fields = ["id", "nick", "name", "city", "city__pindex", "address",
            "created_at"]
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class":
            "table table-striped table-sm border-info \
                 table-hover shadow"
        }

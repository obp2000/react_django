from django_tables2 import Table, Column, LinkColumn
from django_tables2 import A  # alias for Accessor
from django.utils.translation import gettext_lazy as _
from .models import Customer


class CustomerTable(Table):

    nick = Column(linkify=True)
    name = Column(linkify=True)
    delete = LinkColumn("customer-delete", text=_("Delete"),
                        args=[A("pk")], verbose_name='',
                        attrs={"a": {"class":
                                     "btn btn-outline-primary btn-sm"}})

    class Meta:
        model = Customer
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class":
                 "table table-sm table-striped table-bordered table-hover"}

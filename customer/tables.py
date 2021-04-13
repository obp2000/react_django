from django_tables2 import Table, Column, LinkColumn, A, TemplateColumn
# from django_tables2 import A  # alias for Accessor
from django.utils.translation import gettext_lazy as _
from .models import Customer


class CustomerTable(Table):

    nick = Column(linkify=True)
    name = Column(linkify=True)
    # delete = LinkColumn("customer-delete", text=_("Delete"),
    #                     args=[A("pk")], verbose_name='',
    #                     attrs={"a": {"class":
    #                                  "btn btn-outline-primary btn-sm"}})
    delete = TemplateColumn(template_name="customer/delete_column.html", verbose_name='')


    class Meta:
        model = Customer
        fields = ["id", "nick", "name", "city", "created_at", "updated_at"]
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class":
                 "table table-primary table-striped table-sm border-info table-hover"}

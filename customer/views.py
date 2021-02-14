"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from .models import Customer
from .serializers import CustomerSerializer
from .tables import CustomerTable
from .filters import CustomerFilter
from .forms import (CustomerForm, CustomerFilterFormHelper,
                    DeleteCustomerForm)


class CustomerViewSet(ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = ['nick', 'name', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]


class CustomerList(SingleTableMixin, FilterView):
    model = Customer
    table_class = CustomerTable
    template_name_suffix = '_list'
    paginate_by = 5
    filterset_class = CustomerFilter

    # def get_form_class(self):
    #     return CustomerFilterForm

    extra_context = {'customer_filter_helper': CustomerFilterFormHelper}


class CustomerCreate(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')
    # extra_context = {'customer_helper': CustomerFormHelper}
    success_message = "%s %s %s." % (_("customer").title(),
                                     _("was created"),
                                     _("successfully"))


class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    # success_message = "%s %s %s." % (_("customer").title(),
    #                                  _("was updated"),
    #                                  _("successfully"))
    success_message = _("%(nick)s was updated successfully")

    # def get_success_message(self, cleaned_data):
    #     self.success_message = "%(nick)s %(was_updated)s %(successfully)s"
    #     return self.success_message % {
    #         "nick": cleaned_data["nick"],
    #         "was_updated": _("was updated"),
    #         "successfully": _("successfully")
    #         }
    # fields = '__all__'
    # extra_context = {'customer_helper': CustomerFormHelper}


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')
    # form_class = DeleteCustomerForm
    extra_context = {'form': DeleteCustomerForm}

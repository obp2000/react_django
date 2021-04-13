"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from bootstrap_modal_forms.generic import BSModalDeleteView
from .models import Customer
from .serializers import CustomerSerializer
from .tables import CustomerTable
from .filters import CustomerFilter
from .forms import CustomerForm, CustomerFilterFormHelper, DeleteCustomerForm


class CustomerViewSet(ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    # queryset = Customer.objects.all()
    queryset = Customer.objects.select_related("city")
    serializer_class = CustomerSerializer
    search_fields = ['nick', 'name', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]


class CustomerList(SingleTableMixin, FilterView):
    table_data = Customer.objects.select_related("city")
    table_class = CustomerTable
    table_pagination = {'per_page': 5}
    template_name_suffix = '_list'
    filterset_class = CustomerFilter
    extra_context = {'customer_filter_helper': CustomerFilterFormHelper, 
                     'delete_customer_form': DeleteCustomerForm}


class CustomerCreate(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')
    success_message = _("%(nick)s was created successfully")


class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_message = _("%(nick)s was updated successfully")


class CustomerDelete(BSModalDeleteView):
    model = Customer
    extra_context = {'form': DeleteCustomerForm}
    success_url = reverse_lazy('customer-list')
    success_message = _("%(nick)s was deleted successfully")

"""
API endpoints that allow models to be viewed or edited.
"""
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
# from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext as _
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from bootstrap_modal_forms.generic import BSModalDeleteView
from react_django.utils import AccessMixin
from react_django.forms import DeleteFormHelper, DeleteObjectForm, \
    FilterFormHelper
from .models import Customer
from .serializers import CustomerSerializer
from .tables import CustomerTable
from .filters import CustomerFilter
from .forms import CustomerForm, \
    CustomerFormWitDisabledName, CustomerFormHelper


class CustomerViewSet(ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.select_related("city")
    serializer_class = CustomerSerializer
    search_fields = ['nick', 'name', 'address']
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]


class CustomerList(SingleTableMixin, FilterView):
    queryset = Customer.objects.select_related("city")
    table_class = CustomerTable
    table_pagination = {'per_page': 5}
    template_name = "object_list.html"
    filterset_class = CustomerFilter
    extra_context = {'filter_helper': FilterFormHelper(
        filter_fields=CustomerFilter._meta.fields),
                     'delete_object_form': DeleteObjectForm,
                     'delete_path_name': 'customer:customer-delete',
                     'table_title': _("customers").capitalize(),
                     'new_url': reverse_lazy('customer:customer-new'),
                     'list_url': reverse_lazy('customer:customer-list')}


class CustomerCreate(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "object_form.html"
    success_url = reverse_lazy('customer:customer-list')
    success_message = _("%(nick)s was created successfully")
    extra_context = {'object_form_helper': CustomerFormHelper}


class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = "object_form.html"
    # form_class = CustomerForm
    # permission_required = "customer.change_customer_name"
    # login_url = reverse_lazy('login')
    # handle_no_permission = AccessMixin.handle_no_permission
    success_message = _("%(nick)s was updated successfully")
    extra_context = {'object_form_helper': CustomerFormHelper}

    def get_form_class(self):
        return CustomerForm if self.request.user.has_perm("customer.change_customer_name") \
            else CustomerFormWitDisabledName


class CustomerDelete(BSModalDeleteView):
    model = Customer
    extra_context = {'form': DeleteObjectForm,
                     'delete_form_helper': DeleteFormHelper}
    template_name = "object_confirm_delete.html"
    success_url = reverse_lazy('customer:customer-list')
    success_message = "%s %s" % (_("customer").capitalize(), _("was deleted successfully"))

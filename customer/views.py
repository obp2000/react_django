from bootstrap_modal_forms.generic import BSModalDeleteView
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
# from rest_framework import permissions
# from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from react_django.form_helpers import DeleteFormHelper, FilterFormHelper
from react_django.forms import DeleteObjectForm

from .filters import CustomerFilter
from .form_helpers import CustomerFormHelper
from .forms import CustomerForm
from .models import Customer
from .tables import CustomerTable


class CustomerQuerysetMixin(object):
    queryset = Customer.objects.select_related("city")


class CustomerSuccessUrlMixin(object):
    success_url = reverse_lazy('customer:list')


class CustomerEditMixin(CustomerSuccessUrlMixin, CustomerQuerysetMixin):
    form_class = CustomerForm
    template_name = "object_form.html"
    extra_context = {'object_form_helper': CustomerFormHelper}


class CustomerList(CustomerQuerysetMixin, SingleTableMixin, FilterView):
    table_class = CustomerTable
    table_pagination = {'per_page': 5}
    template_name = "object_list.html"
    filterset_class = CustomerFilter
    extra_context = {
        'filter_helper':
        FilterFormHelper(filter_fields=CustomerFilter._meta.fields),
        'delete_object_form': DeleteObjectForm,
        'delete_path_name': 'customer:delete',
        'table_title': _("customers").capitalize(),
        'new_url': reverse_lazy('customer:new'),
        'list_url': reverse_lazy('customer:list'),
        'total_count': Customer.objects.count()
    }


class CustomerCreate(CustomerEditMixin, SuccessMessageMixin, CreateView):
    success_message = _("%(nick)s was created successfully")


class CustomerUpdate(CustomerEditMixin, SuccessMessageMixin, UpdateView):
    success_message = _("%(nick)s was updated successfully")


class CustomerDelete(CustomerSuccessUrlMixin, CustomerQuerysetMixin,
                     BSModalDeleteView):
    extra_context = {
        'form': DeleteObjectForm,
        'delete_form_helper': DeleteFormHelper
    }
    template_name = "object_confirm_delete.html"
    success_message = (f'{_("customer").capitalize()} '
                       f'{_("was deleted successfully")}')

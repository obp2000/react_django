from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin

from .models import City, Customer

admin.site.register(City)

# from .forms import CustomerForm

# admin.site.register(Customer)


@admin.register(Customer)
class CustomerAdmin(AjaxSelectAdmin):

    form = make_ajax_form(
        Customer,
        {
            # fieldname: channel_name
            'city': 'city'
        })


# @admin.register(Customer)
# class CustomerAdmin(AjaxSelectAdmin):
#     form = CustomerForm

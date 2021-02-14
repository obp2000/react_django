from django.contrib import admin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
from .models import Customer
# from .forms import CustomerForm

# admin.site.register(Customer)


@admin.register(Customer)
class CustomerAdmin(AjaxSelectAdmin):

    form = make_ajax_form(Customer, {
        # fieldname: channel_name
        'city': 'city'
    })

# @admin.register(Customer)
# class CustomerAdmin(AjaxSelectAdmin):
#     form = CustomerForm

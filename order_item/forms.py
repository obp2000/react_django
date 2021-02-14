from django.forms.models import BaseInlineFormSet
from django.forms import ModelForm, DecimalField, IntegerField, CharField, \
                         HiddenInput
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit, Layout, HTML, Row, MultiField,
                                 Fieldset, Column, Field)
from crispy_forms.bootstrap import UneditableField
from django_select2.forms import ModelSelect2Widget
# from django_select2.views import AutoResponseView
# from ajax_select.helpers import make_ajax_field
# from .lookup import ProductLookup
# from order.forms_with_sums import FormWithSums
from .models import OrderItem


class ProductWidget(ModelSelect2Widget):
    search_fields = ["name__icontains"]

    # def build_attrs1(self, base_attrs, extra_attrs=None):
    #     attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
    #     attrs["price"] = 7778888888
    #     return attrs

    # def label_from_instance1(self, obj):
    #     # return str(obj.title).upper()
    #     return "%s %s/%s/%s" % (obj.name, obj.price, obj.density, obj.width,)

    # def build_attrs(self, base_attrs, extra_attrs=None):
    #     print(self.obj)
    #     print('ggggggggggggggggggggggg')
    #     extra_attrs['data-price'] = 7777
    #     return super().build_attrs(base_attrs, extra_attrs)

    # def extra_data_from_instance(self, obj):
    #     print('gggggggggggggg')
    #     return {
    #         "stages": 88888,
    #     }


class OrderItemForm(ModelForm):

    def __init__(self, * args, ** kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'sum': '%.2f' % instance.sum,
                                 'weight': instance.weight,
                                 'density': instance.density,
                                 'width': instance.width}
        super().__init__(*args, **kwargs)

    sum = CharField(required=False, disabled=True)
    weight = CharField(required=False, disabled=True)
    density = IntegerField(required=False, disabled=True, widget=HiddenInput())
    width = IntegerField(required=False, disabled=True, widget=HiddenInput())

    class Meta:
        model = OrderItem
        fields = '__all__'
        widgets = {
            "product": ProductWidget
        }

# class OrderItemFormSetHelper(FormHelper):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.template = 'bootstrap4/table_inline_formset.html'
#         # self.disable_csrf = True
#         self.form_tag = False


class BaseOrderItemInlineFormSet(BaseInlineFormSet):

    def __init__(self, * args, ** kwargs):
        super().__init__(* args, ** kwargs)
        self.helper = FormHelper()
        self.helper.template = 'order_item/table_inline_formset.html'
        self.helper.form_class = ''
        # self.disable_csrf = True
        self.helper.form_tag = False

        # self.queryset = OrderItem.order_items.all_with_sum()

    # queryset = OrderItem.order_items.all_with_sum()

    # def add_fields(self, form, index):
    #     super().add_fields(form, index)
    #     form.fields["sum"] = DecimalField(label=_('sum').title(),
    #                                       required=False,
    #                                       disabled=True,
    #                                       initial='%.2f' % form.instance.sum)
    #     form.fields["weight"] = IntegerField(label=_('weight').title(),
    #                                          required=False,
    #                                          disabled=True,
    #                                          initial=form.instance.weight)

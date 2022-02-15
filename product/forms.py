from django.forms import BooleanField, ModelForm
from django.utils.translation import gettext_lazy as _
from react_django.forms import CharFieldDisabled

from .models import Product


class ProductForm(ModelForm):
    id = CharFieldDisabled()
    fleece = BooleanField(required=False)
    price_rub_m = CharFieldDisabled(label=_('meter price').capitalize())
    density_for_count = CharFieldDisabled(
        label=_('density for count').capitalize())
    meters_in_roll = CharFieldDisabled(label=_('meters in roll').capitalize())

    def full_clean(self):
        # print('self.data: ', self.data)
        data_dict = self.data.dict()
        blank_fields = {key: None for key, value in data_dict.items() if value == 'None'}
        data_dict.update(blank_fields)
        self.data = data_dict
        return super().full_clean()

    class Media:
        js = ('js/product_form.js', )

    class Meta:
        model = Product
        fields = '__all__'

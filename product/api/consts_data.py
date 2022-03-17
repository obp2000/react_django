from ..forms import ProductForm
from ..models import Consts, Product
from .serializers import ProductTypeSerializer

consts_data = {
    'name_singular': Product._meta.verbose_name.capitalize(),
    'name_plural': Product._meta.verbose_name_plural.capitalize(),
    'product_type': {
        'label': ProductForm().fields['product_type'].label,
        'choices': ProductTypeSerializer.options()},
    'new_image': {'label': ProductForm().fields['image'].label},
    'prices': {'label': ProductForm().fields['price_rub_m'].label},
    'density_for_count': {'label': ProductForm().fields['density_for_count'].label},
    'meters_in_roll': {'label': ProductForm().fields['meters_in_roll'].label},
    'Consts': Consts
    }

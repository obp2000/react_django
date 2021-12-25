from django.forms import DecimalField, IntegerField, ModelForm
from django.utils.translation import gettext_lazy as _


class FormWithSums(ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance and instance.id:
            kwargs['initial'] = {'sum': f'{instance.sum:.2f}',
                                 'weight': instance.weight}
        super().__init__(*args, **kwargs)

    sum = DecimalField(label=_('sum').title(),
                       required=False,
                       disabled=True)
    weight = IntegerField(label=_('weight').title(),
                          required=False,
                          disabled=True)

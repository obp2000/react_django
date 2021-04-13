from django.db.models import Model, CharField, IntegerField, \
     PositiveIntegerField, DateTimeField, DecimalField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def product_images_path(instance, filename):
    return 'product/image/{0}/{1}'.format(instance.id, filename)


class Product(Model):
    name = CharField(_('name'), max_length=255)
    price = IntegerField(_('price'))
    weight = DecimalField(_('weight'), max_digits=4, decimal_places=2,
                          blank=True, null=True)
    width = PositiveIntegerField(_('width'), blank=True, null=True)
    density = PositiveIntegerField(_('density'), blank=True, null=True)
    dollar_price = DecimalField(_('dollar_price'), max_digits=4,
                                decimal_places=2, blank=True, null=True)
    dollar_rate = DecimalField(_('dollar_rate'), max_digits=5,
                               decimal_places=2, blank=True, null=True)
    width_shop = PositiveIntegerField(_('width_shop'), blank=True, null=True)
    density_shop = PositiveIntegerField(_('density_shop'), blank=True,
                                        null=True)
    weight_for_count = PositiveIntegerField(_('weight_for_count'), blank=True,
                                            null=True)
    length_for_count = DecimalField(_('length_for_count'), max_digits=5,
                                    decimal_places=2, blank=True, null=True)
    price_pre = PositiveIntegerField(_('price_pre'), blank=True, null=True)
    image = ImageField(_('image'), upload_to=product_images_path, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    @property
    def one_m_weight(self):
        return (self.density or 0) * (self.width or 0) / 100
    
    @property
    def price_rub_m(self):
        return (self.dollar_price or 0) * (self.dollar_rate or 0) * \
               (self.density or 0) * (self.width or 0) / 100000
    # price_rub_m.blank = True
    # price_rub_m.verbose_name = _('sum555')
    # price_rub_m = property(price_rub_m)

    @property
    def density_for_count(self):
        if (self.weight_for_count or 0) > 0 and (self.length_for_count or 0) > 0 and (self.width or 0) > 0:
            return self.weight_for_count / self.length_for_count / self.width * 100
        else:
            return 0

    @property        
    def meters_in_roll(self):
        if (self.weight or 0) > 0 and (self.density or 0) > 0 and (self.width or 0) > 0: 
            return self.weight * 100000 / self.density / self.width
        else:
            return 0

    def get_absolute_url(self):
        return reverse('product-update', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'products'
        ordering = ['name']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name

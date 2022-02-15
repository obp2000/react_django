from django.db.models import (SET_NULL, BooleanField, CharField, DateTimeField,
                              DecimalField, ForeignKey, ImageField,
                              IntegerField, Model, PositiveIntegerField)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from react_django.utils import make_label

from .contents import Contents
# from .managers import ProductManager
from .product_type import ProductType
from .threads import Threads


def product_images_path(instance, filename):
    return f'product/image/{instance.id}/{filename}'


class Product(Model):
    name = CharField(_('name'), max_length=255)
    product_type = ForeignKey(ProductType,
                              SET_NULL,
                              blank=True,
                              null=True,
                              verbose_name=_('product_type'))
    threads = PositiveIntegerField(_('threads'),
                                   choices=Threads.choices,
                                   blank=True,
                                   null=True)
    contents = PositiveIntegerField(_('contents'),
                                    choices=Contents.choices,
                                    blank=True,
                                    null=True)
    fleece = BooleanField(_('fleece'), blank=True, null=True)
    price = IntegerField(_('price'))
    weight = DecimalField(_('weight'),
                          max_digits=4,
                          decimal_places=2,
                          blank=True,
                          null=True)
    width = PositiveIntegerField(_('width'), blank=True, null=True)
    density = PositiveIntegerField(_('density'), blank=True, null=True)
    dollar_price = DecimalField(_('dollar_price'),
                                max_digits=4,
                                decimal_places=2,
                                blank=True,
                                null=True)
    dollar_rate = DecimalField(_('dollar_rate'),
                               max_digits=5,
                               decimal_places=2,
                               blank=True,
                               null=True)
    width_shop = PositiveIntegerField(_('width_shop'), blank=True, null=True)
    density_shop = PositiveIntegerField(_('density_shop'),
                                        blank=True,
                                        null=True)
    weight_for_count = PositiveIntegerField(_('weight_for_count'),
                                            blank=True,
                                            null=True)
    length_for_count = DecimalField(_('length_for_count'),
                                    max_digits=5,
                                    decimal_places=2,
                                    blank=True,
                                    null=True)
    price_pre = PositiveIntegerField(_('price_pre'), blank=True, null=True)
    image = ImageField(_('image'), upload_to=product_images_path, blank=True)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    # objects = ProductManager()

    @property
    def get_product_type_display(self):
        return str(self.product_type) if self.product_type else ''

    @property
    def one_m_weight(self):
        return (int(self.density * self.width / 100) if
            self.density and self.width else 0)

    @property
    def price_rub_m(self):
        return (self.dollar_price * self.dollar_rate * self.one_m_weight / 1000
            if self.dollar_price and self.dollar_rate else 0)

    @property
    def density_for_count(self):
        return (self.weight_for_count / self.length_for_count / self.width * 100
            if self.weight_for_count and self.length_for_count and self.width
            else 0)

    @property
    def meters_in_roll(self):
        return self.weight * 1000 / self.one_m_weight if self.weight else 0

    def get_absolute_url(self):
        return reverse('product:update', kwargs={'pk': self.pk})

    def long_str(self):
        labels_map = {'product_type': str(self.product_type),
                      'threads': self.get_threads_display,
                      'fleece': str(Product._meta.get_field('fleece').verbose_name),
                      'contents': self.get_contents_display,
                      'name': self.name}
        return make_label(self, labels_map)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.long_str()

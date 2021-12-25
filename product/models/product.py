from django.db.models import (SET_NULL, CharField, DateTimeField, DecimalField,
                              ForeignKey, ImageField, IntegerField, Model,
                              PositiveIntegerField)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .contents import Contents
from .managers import ProductManager
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

    # products = ProductQuerySet.as_manager()
    products = ProductManager()

    def threads_display(self):
        return self.get_threads_display() if self.threads else ''

    def contents_display(self):
        return self.get_contents_display() if self.contents else ''

    def get_absolute_url(self):
        return reverse('product-update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return (f'{str(self.product_type)} {self.threads_display()} '
                f'{self.contents_display()} {self.name}')

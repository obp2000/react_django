from django.db.models import Model, CharField, IntegerField, \
     PositiveIntegerField, DateTimeField, DecimalField, ForeignKey, \
     SET_NULL, ImageField, QuerySet, ExpressionWrapper, F, \
     Case, When, IntegerChoices, ManyToManyField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ProductType(Model):
    name = CharField(_('name'), max_length=255)
    created_at = DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('type')
        verbose_name_plural = _('types')

    def __str__(self):
        return self.name


class Threads(IntegerChoices):
    TWO_THREADS = 1, _('two threads')
    THREE_THREADS = 2, _('three threads')
    __empty__ = _('(Unknown)')


class Contents(IntegerChoices):
    LYCRA = 1, _('with lycra')
    COTTON = 2, _('100% cotton')
    __empty__ = _('(Unknown)')


class ProductQuerySet(QuerySet):
    one_m_weight = ExpressionWrapper(F('density') * F('width') / 100,
                                     output_field=IntegerField())

    price_rub_m = ExpressionWrapper(F('dollar_price') * F('dollar_rate') * F('one_m_weight') / 1000,
                                    output_field=IntegerField())


    density_for_count = Case(When(length_for_count__gt=0, width__gt=0,
                                  then=F('weight_for_count') / F('length_for_count') /
                                  F('width') * 100),
                             output_field=IntegerField())

    meters_in_roll = Case(When(one_m_weight__gt=0,
                               then=F('weight') * 1000 / F('one_m_weight')),
                          output_field=DecimalField(decimal_places=2))

    def details(self):
        return self.select_related("product_type").annotate(
            one_m_weight=self.one_m_weight,
            price_rub_m=self.price_rub_m,
            density_for_count=self.density_for_count,
            meters_in_roll=self.meters_in_roll)


def product_images_path(instance, filename):
    return 'product/image/{0}/{1}'.format(instance.id, filename)


class Product(Model):
    name = CharField(_('name'), max_length=255)
    product_type = ForeignKey(ProductType, SET_NULL, blank=True, null=True,
                              verbose_name=_('product_type'))
    threads = PositiveIntegerField(_('threads'), choices=Threads.choices, blank=True, null=True)
    contents = PositiveIntegerField(_('contents'), choices=Contents.choices, blank=True, null=True)
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

    products = ProductQuerySet.as_manager()

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
        return " ".join([str(self.product_type), self.threads_display(), self.contents_display(), \
                         self.name,])

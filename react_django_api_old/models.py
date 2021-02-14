from django.db.models import (Model, CharField, IntegerField,
                              DateTimeField, DecimalField, ImageField,
                              ForeignKey, SET_NULL, CASCADE,
                              Sum, F,
                              QuerySet, Manager)
from django.utils.translation import gettext as _
from django_integer_enum.enums import Enum
from django_integer_enum.fields import EnumIntegerField
from customer.models import Customer
from delivery_type.models import DeliveryType
# from city.models import City


# class City(Model):
#     pindex = CharField(primary_key=True, max_length=6)
#     city = CharField(unique=True, max_length=80)

#     class Meta:
#         managed = False
#         db_table = 'cities'
#         ordering = ['city']

#     def __str__(self):
#         """String for representing the Model object."""
#         return self.city


# class Customer(Model):
#     nick = CharField(max_length=255)
#     name = CharField(max_length=255, blank=True, null=True)
#     city = ForeignKey(City, on_delete=SET_NULL, null=True,
#                       blank=True, db_column='pindex')
#     address = CharField(max_length=255, blank=True, null=True)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)

#     class Meta:
#         managed = False
#         db_table = 'customers'
#         ordering = ['nick']

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.nick} ({self.name})'


# def product_images_path(instance, filename):
#     return 'product/image/{0}/{1}'.format(instance.id, filename)


# class Product(Model):
#     name = CharField(max_length=255)
#     price = IntegerField(null=True, blank=True)
#     weight = DecimalField(max_digits=4, decimal_places=2,
#                           blank=True, null=True)
#     width = IntegerField(blank=True, null=True)
#     density = IntegerField(blank=True, null=True, default=0)
#     dollar_price = DecimalField(max_digits=4, decimal_places=2,
#                                 blank=True, null=True, default=0)
#     dollar_rate = DecimalField(max_digits=5, decimal_places=2,
#                                blank=True, null=True, default=0)
#     width_shop = IntegerField(blank=True, null=True, default=0)
#     density_shop = IntegerField(blank=True, null=True, default=0)
#     weight_for_count = IntegerField(blank=True, null=True, default=0)
#     length_for_count = DecimalField(max_digits=5, decimal_places=2,
#                                     blank=True, null=True, default=0)
#     price_pre = IntegerField(blank=True, null=True, default=0)
#     image = ImageField(upload_to=product_images_path, blank=True, null=True)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)

#     class Meta:
#         managed = False
#         db_table = 'products'
#         ordering = ['name']        


# class DeliveryType(Enum):
#     POST = 0
#     DEL_LIN = 1
#     PEK = 2
#     GTD = 3
#     ENERGIA = 4
#     GDE = 5
#     RATEK = 6
#     BAIKAL = 7
#     SDEK_P = 8

#     local = (
#         _('Почта России'),
#         _('Деловые линии'),
#         _('ПЭК'),
#         _('GTD (Кит)'),
#         _('Энергия'),
#         _('ЖелДорЭкспедиция'),
#         _('Ратэк'),
#         _('Байкал Сервис'),
#         _('СДЭК Посылочка'),
#     )


# class OrderQuerySet(QuerySet):
#     def all_with_sum(self):
#         return self.annotate(sum=Sum(F('order_items__price')
#                              * F('order_items__amount')))


# class Order(Model):
#     customer = ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)
#     post_cost = IntegerField(blank=True, null=True, default=0)
#     packet = IntegerField(blank=True, null=True, default=0)
#     delivery_type = EnumIntegerField(enum_choices=DeliveryType)
#     address = CharField(max_length=255, blank=True, null=True)
#     gift = CharField(max_length=255, blank=True, null=True)

#     objects = Manager()
#     orders = OrderQuerySet.as_manager()

#     # @classmethod
#     # def test1(cls):
#     #     return cls.objects.annotate(sum=Sum(F('order_items__price')
#     #                                 * F('order_items__amount')))

#     class Meta:
#         managed = False
#         db_table = 'orders'
#         ordering = ['-created_at']


# class OrderItem(Model):
#     order = ForeignKey(Order, related_name='order_items',
#                        on_delete=CASCADE, null=True, blank=True)
#     product = ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
#     amount = DecimalField(max_digits=5, decimal_places=2,
#                           blank=True, null=True, default=0)
#     price = DecimalField(max_digits=6, decimal_places=2, blank=True,
#                          null=True, default=0)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)

#     class Meta:
#         managed = False
#         db_table = 'order_items'

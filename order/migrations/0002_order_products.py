# Generated by Django 3.1.4 on 2021-05-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order_item', '0001_initial'),
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order_item.OrderItem', to='product.Product'),
        ),
    ]
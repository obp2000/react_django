# Generated by Django 3.1.4 on 2021-05-05 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_item', '0001_squashed_0003_auto_20210504_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'order_item', 'verbose_name_plural': 'order_items'},
        ),
    ]
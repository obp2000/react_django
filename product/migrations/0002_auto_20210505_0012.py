# Generated by Django 3.1.4 on 2021-05-05 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_squashed_0003_auto_20210504_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
# Generated by Django 3.1.4 on 2022-01-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20220122_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city', 'pindex'], 'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
    ]

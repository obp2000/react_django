# Generated by Django 3.1.4 on 2022-01-21 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_city1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
    ]

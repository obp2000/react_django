# Generated by Django 3.1.4 on 2021-05-23 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('city', '0001_initial'),
    # ]

    operations = [
        # migrations.CreateModel(
        #     name='City',
        #     fields=[
        #         ('pindex', models.CharField(max_length=6, primary_key=True,
        #                                     serialize=False, verbose_name='pindex')),
        #         ('city', models.CharField(max_length=80,
        #                                   unique=True, verbose_name='name')),
        #     ],
        #     options={
        #         'verbose_name': 'city',
        #         'verbose_name_plural': 'cities',
        #         'ordering': ['city'],
        #     },
        # ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255, verbose_name='nick')),
                ('name', models.CharField(blank=True,
                                          max_length=255, verbose_name='name')),
                ('address', models.CharField(blank=True,
                                             max_length=255, verbose_name='address')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated_at')),
                ('city', models.ForeignKey(blank=True, db_column='pindex', null=True,
                                           on_delete=django.db.models.deletion.SET_NULL, to='city.city', verbose_name='city')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ['nick'],
                'permissions': [('change_customer_name', 'Can change the name of customers'), ('change_customer_city', 'Can change the city of customers')],
            },
        ),
        # migrations.AlterField(
        #     model_name='customer',
        #     name='city',
        #     field=models.ForeignKey(blank=True, db_column='pindex', null=True,
        #                             on_delete=django.db.models.deletion.SET_NULL, to='customer.city', verbose_name='city'),
        # ),
    ]
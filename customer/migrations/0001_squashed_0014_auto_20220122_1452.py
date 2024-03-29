# Generated by Django 3.1.4 on 2022-05-19 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('customer', '0001_initial'), ('customer', '0002_auto_20220121_2248'), ('customer', '0003_change_primary_key'), ('customer', '0004_auto_20220122_0013'), ('customer', '0005_customer_city1'), ('customer', '0006_remove_customer_city'), ('customer', '0007_auto_20220122_0127'), ('customer', '0008_auto_20220122_0129'), ('customer', '0009_auto_20220122_0131'), ('customer', '0010_auto_20220122_0148'), ('customer', '0011_auto_20220122_0206'), ('customer', '0012_remove_city_citykey'), ('customer', '0013_auto_20220122_1442'), ('customer', '0014_auto_20220122_1452')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('pindex', models.CharField(blank=True, max_length=6, null=True, verbose_name='pindex')),
                ('city', models.CharField(max_length=80, verbose_name='name')),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('opsname', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ['city', 'pindex'],
                'index_together': {('city', 'pindex')},
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255, verbose_name='nick')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.city', verbose_name='city')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ['-updated_at'],
                'permissions': [('change_customer_name', 'Can change the name of customers'), ('change_customer_city', 'Can change the city of customers')],
            },
        ),
    ]

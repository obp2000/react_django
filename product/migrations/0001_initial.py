# Generated by Django 3.1.4 on 2022-01-04 11:16

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import product.models.product


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('threads', models.PositiveIntegerField(blank=True, choices=[(1, 'two threads'), (2, 'three threads')], null=True, verbose_name='threads')),
                ('contents', models.PositiveIntegerField(blank=True, choices=[(None, '-'), (1, 'with lycra'), (2, '100% cotton')], null=True, verbose_name='contents')),
                ('price', models.IntegerField(verbose_name='price')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='weight')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='width')),
                ('density', models.PositiveIntegerField(blank=True, null=True, verbose_name='density')),
                ('dollar_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='dollar_price')),
                ('dollar_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='dollar_rate')),
                ('width_shop', models.PositiveIntegerField(blank=True, null=True, verbose_name='width_shop')),
                ('density_shop', models.PositiveIntegerField(blank=True, null=True, verbose_name='density_shop')),
                ('weight_for_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='weight_for_count')),
                ('length_for_count', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='length_for_count')),
                ('price_pre', models.PositiveIntegerField(blank=True, null=True, verbose_name='price_pre')),
                ('image', models.ImageField(blank=True, upload_to=product.models.product.product_images_path, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('product_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.producttype', verbose_name='product_type')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
            managers=[
                ('products', django.db.models.manager.Manager()),
            ],
        ),
    ]

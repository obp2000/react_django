# Generated by Django 3.1.4 on 2021-05-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210505_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contents',
            field=models.PositiveIntegerField(blank=True, choices=[(None, '(Unknown)'), (1, 'with lycra'), (2, '100% cotton')], default='(Unknown)', null=True, verbose_name='contents'),
        ),
    ]

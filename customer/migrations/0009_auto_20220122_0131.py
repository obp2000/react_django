# Generated by Django 3.1.4 on 2022-01-21 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20220122_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.city', verbose_name='city'),
        ),
    ]
# Generated by Django 3.1.4 on 2022-01-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20220122_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=80, verbose_name='name'),
        ),
    ]

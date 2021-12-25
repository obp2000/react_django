# Generated by Django 3.1.4 on 2021-12-25 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('pindex', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='pindex')),
                ('city', models.CharField(max_length=80, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ['city'],
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(blank=True, db_column='pindex', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.city', verbose_name='city'),
        ),
    ]
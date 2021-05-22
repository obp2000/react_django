# Generated by Django 3.1.4 on 2021-05-04 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_squashed_0011_auto_20210504_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255, verbose_name='nick')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('city', models.ForeignKey(blank=True, db_column='pindex', null=True, on_delete=django.db.models.deletion.SET_NULL, to='city.city', verbose_name='city')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'customers',
                'ordering': ['nick'],
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]

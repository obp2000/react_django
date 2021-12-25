# Generated by Django 3.1.4 on 2021-05-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]

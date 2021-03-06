# Generated by Django 3.1.4 on 2021-05-04 23:43

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
                'db_table': 'cities',
                'ordering': ['city'],
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='city',
            table=None,
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['pindex'], name='city_city_pindex_117dca_idx'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['city'], name='city_city_city_6f2a6d_idx'),
        ),
        migrations.RemoveIndex(
            model_name='city',
            name='city_city_pindex_117dca_idx',
        ),
        migrations.RemoveIndex(
            model_name='city',
            name='city_city_city_6f2a6d_idx',
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(db_index=True, max_length=80, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=80, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(db_index=True, max_length=80, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=80, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=80, unique=True, verbose_name='name'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0005_auto_20151023_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Master_Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website_name', models.CharField(max_length=100, blank=True)),
                ('city_id', models.CharField(max_length=500, blank=True)),
                ('city_name', models.CharField(max_length=500, blank=True)),
                ('make_id', models.CharField(max_length=500, blank=True)),
                ('make_name', models.CharField(max_length=500, blank=True)),
                ('model_id', models.CharField(max_length=500, blank=True)),
                ('model_name', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cardetails',
            old_name='makes',
            new_name='car_make',
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='price',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]

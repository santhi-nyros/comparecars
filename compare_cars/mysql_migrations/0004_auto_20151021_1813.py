# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0003_auto_20151021_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='car_color',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='car_href',
            field=models.URLField(max_length=5000, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='car_image',
            field=models.ImageField(max_length=500, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='car_model',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='car_title',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='city',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='makes',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.IntegerField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='website_name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]

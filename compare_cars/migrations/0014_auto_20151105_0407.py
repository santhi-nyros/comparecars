# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0013_auto_20151104_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='is_there',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='car_href',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]

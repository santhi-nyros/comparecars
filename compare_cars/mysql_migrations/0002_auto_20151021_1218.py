# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='car_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.CharField(max_length=50),
        ),
    ]

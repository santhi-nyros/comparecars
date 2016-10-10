# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0018_auto_20151105_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='car_image',
            field=models.URLField(max_length=500, blank=True),
        ),
    ]

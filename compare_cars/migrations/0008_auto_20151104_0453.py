# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0007_auto_20151104_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]

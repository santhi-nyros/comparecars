# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0019_auto_20151105_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='keywords',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]

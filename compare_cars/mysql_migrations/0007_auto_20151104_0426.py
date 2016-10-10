# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0006_auto_20151102_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.IntegerField(blank=True),
        ),
    ]

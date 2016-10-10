# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0002_auto_20151021_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

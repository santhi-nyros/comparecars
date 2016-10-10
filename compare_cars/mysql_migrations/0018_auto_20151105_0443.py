# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0017_auto_20151105_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetails',
            name='is_there',
        ),
        migrations.AddField(
            model_name='cardetails',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0014_auto_20151105_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetails',
            name='is_there',
        ),
    ]

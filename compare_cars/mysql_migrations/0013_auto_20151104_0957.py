# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0012_auto_20151104_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardetails',
            old_name='makes',
            new_name='car_make',
        ),
    ]

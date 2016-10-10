# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0016_cardetails_active_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardetails',
            old_name='active_id',
            new_name='is_there',
        ),
    ]

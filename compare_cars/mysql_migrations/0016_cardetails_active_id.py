# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0015_remove_cardetails_is_there'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='active_id',
            field=models.IntegerField(default=0),
        ),
    ]

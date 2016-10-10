# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0011_auto_20151104_0854'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarMakeDetails',
            new_name='CarDetails',
        ),
    ]

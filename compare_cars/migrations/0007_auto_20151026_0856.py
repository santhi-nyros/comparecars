# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0006_carmakedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmakedetails',
            name='model_year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

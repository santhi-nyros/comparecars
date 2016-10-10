# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0009_merge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car_Master_Data',
        ),
        migrations.RenameField(
            model_name='cardetails',
            old_name='car_make',
            new_name='makes',
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='model_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='carmakedetails',
            name='model_year',
            field=models.CharField(default=0, max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carmakedetails',
            name='price',
            field=models.CharField(default=-2022, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]

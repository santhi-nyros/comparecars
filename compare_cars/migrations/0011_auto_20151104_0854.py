# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0010_auto_20151104_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Master_Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website_name', models.CharField(max_length=100, blank=True)),
                ('city_id', models.CharField(max_length=500, blank=True)),
                ('city_name', models.CharField(max_length=500, blank=True)),
                ('make_id', models.CharField(max_length=500, blank=True)),
                ('make_name', models.CharField(max_length=500, blank=True)),
                ('model_id', models.CharField(max_length=500, blank=True)),
                ('model_name', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CarDetails',
        ),
    ]

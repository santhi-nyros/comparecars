# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compare_cars', '0005_auto_20151023_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMakeDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website_name', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('makes', models.CharField(max_length=100, blank=True)),
                ('car_model', models.CharField(max_length=100, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
                ('model_year', models.IntegerField(blank=True)),
                ('car_title', models.CharField(max_length=500, blank=True)),
                ('car_href', models.URLField(max_length=5000, blank=True)),
                ('car_image', models.ImageField(max_length=500, upload_to=b'', blank=True)),
                ('car_color', models.CharField(max_length=50, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

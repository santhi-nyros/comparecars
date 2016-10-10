# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('makes', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('model_year', models.TextField()),
                ('car_title', models.TextField(max_length=500)),
                ('car_href', models.URLField(max_length=5000)),
                ('car_image', models.ImageField(max_length=500, upload_to=b'')),
                ('car_color', models.CharField(max_length=50)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 09:14
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='well_info',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='well_info',
            name='lon',
        ),
        migrations.AddField(
            model_name='well_info',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
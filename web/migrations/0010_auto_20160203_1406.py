# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20160203_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='event_source_datetime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='resource',
            name='event_source_timezone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='resource',
            name='event_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

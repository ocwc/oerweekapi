# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_resource_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0045_resource_resource_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='image',
        ),
    ]

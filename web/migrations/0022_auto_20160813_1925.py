# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-13 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_auto_20160813_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='categories',
        ),
        migrations.AddField(
            model_name='resource',
            name='categories',
            field=models.ManyToManyField(null=True, to='web.Category'),
        ),
    ]
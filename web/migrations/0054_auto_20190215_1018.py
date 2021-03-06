# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-15 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0053_auto_20181024_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.ResourceImage'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='year',
            field=models.IntegerField(blank=True, default=2019, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gscan', '0008_portconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='weakfile',
            name='weakfile',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0004_auto_20170924_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcourse', '0027_auto_20170330_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='agree',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='disagree',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcourse', '0021_auto_20170326_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='university',
            field=models.CharField(default='', max_length=30),
        ),
    ]
